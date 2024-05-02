import requests
get_all_breed = "https://dog.ceo/api/breeds/list/all"


#Api get function will retrieve the information
response = requests.get(get_all_breed)

#to validate whether status code is 200 or not
assert response.status_code == 200

#.json() will convert the reponse to json format
print(response.json()['status'])

print("individual breeds are", '\n')
print("-------------------------------------------------------------------------", '\n')

# For loop will get each breed from all the list of breed
for dog_breed in response.json()['message']:

    breed= response.json()['message'][dog_breed]

    #if values of breed key is <= 1 then it will be considered as individual dof breed
    if len(breed) <= 1:
        print(dog_breed, "- breed count: ", len(breed))
