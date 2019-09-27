import os,sys

parent_dir = os.path.abspath(os.path.dirname(__file__))
packages_dir = os.path.join(parent_dir, 'packages')
sys.path.append(packages_dir)

from datetime import datetime
import myfitnesspal

client = myfitnesspal.Client(os.environ['USER_NAME'], os.environ['PASSWORD'])

def handle(req):
    try:
        day = client.get_date(datetime.now())
        print(day.__dict__)
        totals = day.totals

        return "{} grams of protein, {} calories".format(totals['calories'], totals['protein'])
    except KeyError:
        return "no food logged today yet"
    except Exception as e:
        return "error: {}".format(e)

