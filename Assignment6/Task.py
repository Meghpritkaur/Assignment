#TASK 1: Create a Python dictionary called insta_followers that stores the number of followers for 5 Instagram influencers (use their usernames as keys and follower counts as values). Print the dictionary.
'''
insta_followers={"Virat_kohli":5600000, "Sachin_Tendulkar":6000000, "Kriti _sanon":4500000, "Alia_Bhatt":4800000 , "cristiano":5000000}
print(insta_followers)
'''



#TASK 2: Add a new influencer to your insta_followers dictionary and update the follower count for one existing influencer. Then, delete one influencer from the dictionary and print the updated dictionary.
'''
insta_followers={"Virat_kohli":5600000, "Sachin_Tendulkar":6000000, "Kriti _sanon":4500000, "Alia_Bhatt":4800000 , "cristiano":5000000}
insta_followers["Tech"]=4000000
print(insta_followers)
print("Updated follower:",insta_followers)

insta_followers.pop("cristiano")
print("Delete one follower:",insta_followers)
'''



#TASK 3: Given a dictionary called food_prices with 5 Zomato food items as keys and their prices as values, write code to display all items that cost more than ₹200.
'''
food_prices={"Burger":129,"Pizza":220,"Chinese_combos":499,"Maggie":79,"Shake":100}

for i in food_prices:
    if food_prices[i] > 200:
        print(i, ":", food_prices[i])
'''



#TASK 4: Create two sets: flipkart_users and myntra_users, each containing 5 unique usernames.
# Find and print the set of users who have accounts on both platforms using set intersection.
'''
flipkart_users={"Megh","Priyanka","Riya","Shruti","Priya"}
myntra_users={"Megh","Priyanka","Sam","Aditi","Sakshi"}

print("Have accounts on both platform:",flipkart_users.intersection(myntra_users))
'''



#TASK 5:Write a function get_unique_artists(spotify_playlist1, spotify_playlist2) that takes two sets of artist names and returns a set of all unique artists across both playlists (set union).
# <br><br><em><strong>Hint:</strong> Use the union() method or the | operator for sets.</em>

def get_unique_artists(spotify_playlist1, spotify_playlist2):
    return spotify_playlist1.union(spotify_playlist2)
spotify_playlist1={'Arijit Singh','Diljit dosanjh','Karan Aujla'}
spotify_playlist2={'Badshaah','Atif Aslam','Karan Aujla'}

result=get_unique_artists(spotify_playlist1,spotify_playlist2)
print(result)