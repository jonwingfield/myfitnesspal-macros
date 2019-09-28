import os,sys

parent_dir = os.path.abspath(os.path.dirname(__file__))
packages_dir = os.path.join(parent_dir, 'packages')
sys.path.append(packages_dir)

from datetime import datetime, timedelta
import myfitnesspal

client = myfitnesspal.Client(os.environ['USER_NAME'], os.environ['PASSWORD'])

def handle(event, lambda_context):
    try:
        now_est = datetime.now() - timedelta(hours=5)
        day = client.get_date(now_est)
        totals = day.totals

        return "{} grams of protein, {} calories".format(totals['protein'], totals['calories'])
    except KeyError:
        return "no food logged today yet"
    except Exception as e:
        return "error: {}".format(e)

