import requests, zipfile
from datetime import datetime
import os
import time
import csv
from io import BytesIO
from electricity_data.models import ElectricityData


def schedule_api():
    url = 'http://oasis.caiso.com/oasisapi/SingleZip?resultformat=6&queryname=PRC_RTPD_LMP&version=3&startdatetime=20220701T07:00-0000&enddatetime=20220702T08:00-0000&market_run_id=RTPD&grp_type=ALL_APNODES'

    param = {
        'startdatetime': '20220701T07:00-0000',
        'enddatetime': '20220705T08:00-0000'
    }

    try:
        req = requests.get(url, params=param)
        # print('Downloading Completed')

        # extracting the zip file contents
        zipfile_csv = zipfile.ZipFile(BytesIO(req.content))
        # zipfile.NameToInfo = 'sample'
        filename = list(zipfile_csv.NameToInfo.keys())[0]
        # print(filename)
        zipfile_csv.extractall()

        file = open(filename)
        contents = csv.reader(file)

        # skip old rows
        number = ElectricityData.objects.count()
        if number > 0:
            skip_item = number + 1
        else:
            skip_item = 1
        # insert_records = "INSERT INTO electricity_data (INTERVALSTARTTIME_GMT, INTERVALENDTIME_GMT, OPR_DT, OPR_HR, NODE_ID_XML, NODE_ID, NODE, MARKET_RUN_ID, LMP_TYPE, XML_DATA_ITEM, PNODE_RESMRID, GRP_TYPE, POS, PRC, OPR_INTERVAL, GROUP_NAME) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        # cursor.executemany(insert_records, list(contents)[skip_item::])
        # database.commit()
        count = 0
        for row in list(contents)[skip_item::]:

            count += 1
            # print(row)
        # file.close()
            data = {
                'intervalstarttime_gmt': datetime.fromisoformat(row[0]),
                'intervalendtime_gmt': datetime.fromisoformat(row[1]),
                'opr_dt': datetime.strptime(row[2], '%Y-%m-%d'),
                'opr_hr': int(row[3]),
                'node_id_xml': row[4],
                'node_id': row[5],
                'node': row[6],
                'market_run_id': row[7],
                'lmp_type': row[8],
                'xml_data_item': row[9],
                'pnode_resmrid': row[10],
                'grp_type': row[11],
                'pos': int(row[12]),
                'prc': float(row[13]),
                'opr_interval': int(row[14]),
                'group': int(row[15])
            }
            ElectricityData.objects.create(**data)


        print('insertation completed')
        file.close()
    except Exception as e:
        print(e)
        print('failed, retrying')
    finally:
        time.sleep(100)
        if os.path.exists(filename):
            os.remove(filename)
            print('file remove complete')

