# baseball-machine-learning-project
Using linear regression to predict baseball game attendance.

## Data Source Disclaimer
     The information used here was obtained free of
     charge from and is copyrighted by Retrosheet.  Interested
     parties may contact Retrosheet at "www.retrosheet.org".

# Development environment


# Features of Interest
* Stadium
* Day/Time of day for the game
* Visiting team
* More to consider
    * Weather
    * Game number or time elapsed during season
    * Seasonal team win percentage
    * Double/Triple header

# Cleaning the Data
Starting with the data acquired from Retrosheet we pulled only the features of interest to the project. 

## Cleaned Data File Fields
| Position in Cleaned Data | Position in Source Data | Explanation of Field |
| ------ | ------- | ------ |
| 0 | 0 |  Date in the form "yyyymmdd"|
|1 | 2 | Day of week  ("Sun","Mon","Tue","Wed","Thu","Fri","Sat") |
| 2 | 3 | Visiting team |
| 3 | 5 | Visiting team game number <p><p> For this and the home team game number, ties are counted as games and suspended games are counted from the starting rather than the ending date.|
| 4 | 6 | Home team |
| 5 | 8 | Home team game number |
| 6 | 12 | Day/night indicator ("D" or "N") |
| 7 | 16 | Park ID |
| 8 | 17 | Attendance (unquoted) |
| 9 | 160 | Acquisition information: <ul><li>"Y" -- we have the complete game</li><li> "N" -- we don't have any portion of the game</li><li> "D" -- the game was derived from box score and game story </li><li>"P" -- we have some portion of the game.  We may be missing innings at the beginning, middle and end of the game.</li></ul> |
| 10 | 1 | Number of game: <ul><li>"0" -- a single game </li><li>"1" -- the first game of a double (or triple) header including separate admission doubleheaders</li><li> "2" -- the second game of a double (or triple) header including separate admission doubleheaders</li><li>"3" -- the third game of a triple-header </li><li>"A" -- the first game of a double-header involving 3 teams</li><li> "B" -- the second game of a double-header involving 3 teams</li></ul> |
| 11 | 13 | Completion information. <p> If the game was completed at a later date (either due to a suspension or an upheld protest) this field will include: <ul>"yyyymmdd,park,vs,hs,len" Where <li>yyyymmdd -- the date the game was completed </li><li>park -- the park ID where the game was completed </li><li>vs -- the visitor score at the time of interruption </li><li>hs -- the home score at the time of interruption </li><li>len -- the length of the game in outs at time of interruption</li></ul> All the rest of the information in the record refers to the entire game. </p>|
| 12 | 14 | Forfeit information:<ul><li> "V" -- the game was forfeited to the visiting team </li><li>"H" -- the game was forfeited to the home team </li><li>"T" -- the game was ruled a no-decision</li></ul> |
| 13 | 15 | Protest information: <ul><li>"P" -- the game was protested by an unidentified team </li><li>"V" -- a disallowed protest was made by the visiting team </li><li>"H" -- a disallowed protest was made by the home team </li><li>"X" -- an upheld protest was made by the visiting team </li><li>"Y" -- an upheld protest was made by the home team </li></ul>Note: two of these last four codes can appear in the field (if both teams protested the game). |
| 14 | 9 | Visiting team score (unquoted) |
| 15 | 10 | Home team score (unquoted) |
| 16 | Calculated | Visiting team win percentage |
| 17 | Calculated | Home team win percentage |

# Predicting attendance
   ### Investigations
   We investigated the following features:
   * Stadium - We found a trend once we arranged the stadiums in a nondecreasing order by attendance.
   * Visiting Team - We found a trend once we arranged the teams in a nondecreasing order by attendance.
   * Day - We did not find any trend for the feature.
   * Time - Since there are only two options this is not a good feature to use for regression
   * Day+Time - We were able to merge the two features and find a trend when we arranged the data in a nondecreasing order by attendance.
   * Game number - there seemed to be a spike in the mid season, however we were unable to find a pattern.
   * Month - Following up from the last investigation we looked at each month hoping to find that the summertime games would have a higher attendance. We were unable to find a trend.
   * Seasonal team win percentage - We did not find any pattern to the feature concerning attendance.
   
   ### Features Used
   * Stadium
   * Visiting Team
   * Day+Time
   
   ### Calculations
   The data used to regress is dependent on user input. Once we have user input we pull a subset of the data and regress on it.
