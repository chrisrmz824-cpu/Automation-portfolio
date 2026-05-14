import requests
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

EXCEL_FILE  = "DATA_FILE_CLEAN.xlsx"
PROJECT_ID  = "YOUR_QUALRECRUIT_PROJECT_ID"
BASE_API    = "https://qualrecruit.service.respondentlink.app"
FIELD_JOIN  = "q_join_link_field"
FIELD_CHECK = "q_system_check_field"

GROUP_IDS = [
    "group_id_1",
    "group_id_2",
    "group_id_3",
    "group_id_4",
]

print("=" * 60)
print("  ROBOT QUALRECRUIT - API DIRECTA")
print("=" * 60)
TOKEN = input("\nPega el token Bearer y presiona ENTER:\n> ").strip()
if TOKEN.lower().startswith("bearer "):
    TOKEN = TOKEN[7:].strip()
print()

HEADERS = {
    "Authorization": "Bearer " + TOKEN,
    "Content-Type": "application/json",
    "Origin": "https://www.qualrecruit.app",
    "Referer": "https://www.qualrecruit.app/",
}


def load_data():
    df = pd.read_excel(EXCEL_FILE)
    df_es = df[df["Language"] == "Spanish"].copy()
    df_es["Respondent ID"] = df_es["Respondent ID"].astype(str).str.strip()
    df_es = df_es[df_es["Respondent ID"].str.len() >= 7].copy()
    for col in ["Respondent Join Link", "Respondent System Check Link"]:
        df_es[col] = df_es[col].apply(
            lambda x: str(x).strip()
            if pd.notna(x) and str(x).strip() not in ("", "nan")
            else None
        )
    print("[DATOS] " + str(len(df_es)) + " participantes listos.")
    return df_es.reset_index(drop=True)


def get_respondents_from_group(group_id):
    url = BASE_API + "/vault/" + PROJECT_ID + "/respondent?group=" + group_id
    try:
        r = requests.get(url, headers=HEADERS, timeout=30)
        if r.status_code == 200:
            data = r.json()
            if isinstance(data, list):
                return data
            for key in ("respondents", "data", "items", "results"):
                if key in data:
                    return data[key]
            return data
        return []
    except Exception as e:
        print("[API] Excepcion: " + str(e))
        return []


def update_respondent(resp, group_id, join_link, check_link):
    url = BASE_API + "/vault/" + PROJECT_ID + "/respondent"

    data_fields = []
    if join_link:
        data_fields.append({"Key": FIELD_JOIN, "Value": join_link, "Redacted": False})
    if check_link:
        data_fields.append({"Key": FIELD_CHECK, "Value": check_link, "Redacted": False})
    if not data_fields:
        return False

    # Obtener NewVersion y Version — buscar en todas las variantes de nombre
    new_version = (resp.get("NewVersion") or resp.get("newVersion") or
                   resp.get("new_version") or "")
    version     = (resp.get("Version") or resp.get("version") or "")
    last_updated = (resp.get("LastUpdated") or resp.get("lastUpdated") or
                    resp.get("last_updated") or "")
    full_id     = resp.get("id") or resp.get("Id") or ""
    flags       = resp.get("Flags") or resp.get("flags") or 0

    payload = {
        "Flags": flags,
        "Group": group_id,
        "Id": full_id,
        "LastUpdated": last_updated,
        "Data": data_fields,
    }

    # Solo agregar NewVersion y Version si existen
    if new_version:
        payload["NewVersion"] = new_version
    if version:
        payload["Version"] = version

    try:
        r = requests.put(url, headers=HEADERS, json=payload, timeout=30)
        if r.status_code in (200, 201, 204):
            return True
        print("  [!!] HTTP " + str(r.status_code) + ": " + r.text[:200])
        return False
    except Exception as e:
        print("  [!!] Excepcion: " + str(e))
        return False


def main():
    df_es = load_data()
    if df_es.empty:
        print("[ERROR] No hay datos.")
        return

    print("[API] Obteniendo participantes de todos los grupos...")
    short_to_resp  = {}
    resp_to_group  = {}

    for gid in GROUP_IDS:
        resp_list = get_respondents_from_group(gid)
        print("  " + gid + " -> " + str(len(resp_list)) + " respondents")
        for resp in resp_list:
            full_id = resp.get("id") or resp.get("Id") or ""
            if full_id:
                short = full_id.replace("-", "")[:8].lower()
                short_to_resp[short] = resp
                resp_to_group[short] = gid

    print("[API] Total: " + str(len(short_to_resp)))

    total = len(df_es)
    exitosos = no_encontrados = errores = 0

    print("\n" + "=" * 60)
    print("PROCESANDO " + str(total) + " participantes...")
    print("=" * 60)

    for i, row in df_es.iterrows():
        rid        = row["Respondent ID"].lower().strip()
        name       = str(row.get("Respondent Name", ""))
        join_link  = row["Respondent Join Link"]
        check_link = row["Respondent System Check Link"]

        print("\n[" + str(i + 1) + "/" + str(total) + "] " + rid + " (" + name + ")")

        if rid not in short_to_resp:
            print("  [--] No encontrado.")
            no_encontrados += 1
            continue

        resp  = short_to_resp[rid]
        group = resp_to_group[rid]

        ok = update_respondent(resp, group, join_link, check_link)
        if ok:
            print("  [OK] Actualizado.")
            exitosos += 1
        else:
            errores += 1

    print("\n" + "=" * 60)
    print("RESUMEN FINAL")
    print("  Exitosos:       " + str(exitosos))
    print("  No encontrados: " + str(no_encontrados))
    print("  Errores:        " + str(errores))
    print("  Total:          " + str(total))
    print("=" * 60)
    input("\nPresiona ENTER para cerrar...")


if __name__ == "__main__":
    main()