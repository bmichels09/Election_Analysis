import os
import csv

# Path to CSV files
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize a total vote counter, candidate options, and candidate votes
total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Read election data
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    # Check each row in the CSV file
    for row in file_reader:
        
        # Add 1 to the total vote count
        total_votes += 1

        # Get the candidate name
        candidate_name = row[2]

        # If the candidate does not match any existing candidate, start tracking their votes in the candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Add 1 vote to the candidate's total
        candidate_votes[candidate_name] += 1

# Write results text file
with open(file_to_save,"w") as txt_file:
    
    # Print total vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    print(election_results, end="")

    # Write total vote count to text file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts
    for candidate_name in candidate_votes:
        
        # Get candidate's vote count
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print out the candidate's results on the terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        # Write the result to the text file
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the candidate's votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # If true, then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage

            # Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    # Print the winning candidate with their vote count and percentage
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Write the winning candidate to the text file
    txt_file.write(winning_candidate_summary)