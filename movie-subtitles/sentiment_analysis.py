from datetime import date, datetime, timedelta, time
import pysrt
from textblob import TextBlob
import matplotlib
from matplotlib import style
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.figsize'] = (16.0, 9.0)
style.use('fivethirtyeight')

# Helper Function to create equally divided time intervals
# start - Starting Time
# end - Ending Time
# delta - Interval Period
def create_intervals(start, end, delta):
    curr = start
    while curr <= end:
        curr = (datetime.combine(date.today(), curr) + delta).time()
        yield curr

# Main Function to Get Sentiment Data
# file - srt file location
# delta - time interval in minutes
def get_sentiment(file, delta=2):
    # Reading Subtitle
    subs = pysrt.open(file, encoding='iso-8859-1')
    n = len(subs)
    # List to store the time periods
    intervals = []
    # Start, End and Delta
    start = time(0, 0, 0)
    end = subs[-1].end.to_time()
    delta = timedelta(minutes=delta)
    for result in create_intervals(start, end, delta):
        intervals.append(result)
    # List to store sentiment polarity
    sentiments = []
    
    index = 0
    m = len(intervals)
    # Collect and combine all the text in each time interval
    for i in range(m):
        text = ""
        for j in range(index, n):
            # Finding all subtitle text in the each time interval
            if subs[j].end.to_time() < intervals[i]:
                text += subs[j].text_without_tags + " "
            else:
                break
        # Sentiment Analysis
        blob = TextBlob(text)
        pol = blob.sentiment.polarity
        sentiments.append(pol)
        index = j
    # Adding Initial State
    intervals.insert(0, time(0, 0, 0))
    sentiments.insert(0, 0.0)
    return (intervals, sentiments)

# Utility to find average sentiment
def average(y):
    avg = float(sum(y))/len(y)
    return avg

x, y = get_sentiment("subs/thor.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Thor (2011)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("Thor - 2011.png")

x, y = get_sentiment("subs/ironman.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Iron Man (2008)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("Iron Man - 2008.png")

x, y = get_sentiment("subs/hulk.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("The Incredible Hulk (2008)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("The Incredible Hulk - 2008.png")

x, y = get_sentiment("subs/avengers.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("The Avengers (2012)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("The Avengers - 2012.png")

x, y = get_sentiment("subs/ironman2.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Iron Man 2 (2010)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("Iron Man 2 - 2010.png")

x, y = get_sentiment("subs/cap-america.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Captain America: The First Avenger (2011)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("Captain America: The First Avenger - 2011.png")

x, y = get_sentiment("subs/ironman3.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Iron Man 3 (2013)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("Iron Man 3 - 2013.png")

x, y = get_sentiment("subs/cap-america2.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Captain America: The Winter Soldier (2014)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("Captain America: The Winter Soldier - 2014.png")

x, y = get_sentiment("subs/gotg.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Guardians of the Galaxy (2014)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("Guardians of the Galaxy - 2014.png")

x, y = get_sentiment("subs/avengers2.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Avengers: Age of Ultron (2015)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("Avengers: Age of Ultron - 2015.png")

x, y = get_sentiment("subs/antman.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Ant-Man (2015)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("Ant-Man - 2015.png")

x, y = get_sentiment("subs/cap-america3.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Captain America: Civil War (2016)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("Captain America: Civil War - 2016.png")

x, y = get_sentiment("subs/strange.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Doctor Strange (2016)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("Doctor Strange - 2016.png")

x, y = get_sentiment("subs/gotg2.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Guardians of the Galaxy Vol. 2 (2017)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("Guardians of the Galaxy Vol. 2 - 2017.png")

x, y = get_sentiment("subs/spiderman.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Spider-Man: Homecoming (2017)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("Spider-Man: Homecoming - 2017.png")

x, y = get_sentiment("subs/superman.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Man of Steel (2013)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("Man of Steel - 2013.png")

x, y = get_sentiment("subs/bvs.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Batman v Superman: Dawn of Justice (2016)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("Batman v Superman: Dawn of Justice - 2016.png")

x, y = get_sentiment("subs/suicidesquad.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Suicide Squad (2016)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("Suicide Squad - 2016.png")

x, y = get_sentiment("subs/wonderwoman.srt")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Wonder Woman (2017)", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.savefig("Wonder Woman - 2017.png")