#TASK 1: Create a list called playlist_ids with 5 song IDs (as integers) that you might see in a Spotify playlist, and print the list.
'''
playlist_ids=[101,102,103,104,105]

print("Playlist Ids:",playlist_ids)
'''

#TASK 2: Add two more song IDs to your playlist_ids list using both append() and extend(), then print the updated list.<br><br><em><strong>Hint:</strong> Use append() for a single ID and extend() for adding multiple IDs at once.</em>
'''
playlist_ids=[101,102,103,104,105]
playlist_ids2=[106,107]

playlist_ids.append(106)
print("Append:",playlist_ids)


playlist_ids.extend(playlist_ids2)
print("Extend:",playlist_ids)
'''

#TASK 3: Simulate removing the last played song from your playlist_ids list using pop(), and display the removed ID along with the remaining playlist.
'''
l1=[101,102,103,104,105]

print("Pop the playlist_ids:", l1.pop())
print("Remaining elements:",l1)
'''

#TASK 4: Create a tuple called insta_filters with 4 Instagram filter names (as strings).
# Try to change the first filter name and observe what error you get.<br><br><em><strong>Hint:</strong> Tuples are immutable. 
# Note down the error message.</em>
'''
insta_filters = ("black-white","Aesthetic blur","Valencia")
insta_filters[0]="lark"
print(insta_filters)
print("error message:tuple object does not support item assignment")
'''

#TASK 5: Write a short Python script that takes a scenario (like a list of recent Zomato orders vs a tuple of fixed IPL team names)
# and prints which one should use a list and which should use a tuple, explaining your choice in a comment.

zomato_orders = ["Pizza", "Burger", "Sandwich", "Pasta"]
ipl_teams = ( "GT","PBKS","CSK","MI","RCB","RR","LSG","SRH","KKR","DC")

print("Zomato Orders:", zomato_orders)
print("IPL Teams:", ipl_teams)

