# Election Audit Summary

## Overview of Election Audit
This audit was done to confirm the voting results for the district election, so the election can be certified.

## Election Audit Results
* 369,711 votes were cast in this election.
* The distribution of votes by county was as follows:
  * Arapahoe: 24,801 votes (6.7% of total)
  * Denver: 306,055 votes (82.8%)
  * Jefferson: 38,855 votes (10.5%)
* Denver County had the largest number of votes.
* The number of votes for each candidate was as follows:
  * Charles Casper Stockham: 85,213 votes (23.0% of total)
  * Diana DeGette: 272,892 votes (73.8%)
  * Raymon Anthony Doane: 11,606 votes (3.1%)
* The winner of the election was **Diana DeGette** with 272,892 votes, which was 73.8% of all votes.

## Election Audit Summary
The script used in this audit can be modified to use for any election, as long as the votes are recorded in a CSV file.

For example, if the CSV file uses a different format to record votes, you can edit these two lines so they read the correct rows.

`candidate_name = row[2]`

`county_name = row[1]`

If the script is used for a local election, you can remove the code sections that deal with counties since the county isn't relevant.