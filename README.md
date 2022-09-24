# Exposed APIs as required  
# 1.To Create a Company  
POST request at http://127.0.0.1:8000/Company/ with required bearer token and JSON field in request body  
# without jwt token  
![1](https://user-images.githubusercontent.com/72104547/192118310-1c922298-8751-47c0-9071-e6b2ed1e52a4.png)  
# with jwt authentication token  
![2](https://user-images.githubusercontent.com/72104547/192118337-2d030cfe-01be-4b11-839a-fbbfb7ed1968.png)  
new entry was created  
# 2.Create a Team (Should have company ID in path)  
POST method at http://127.0.0.1:8000/CreateTeam/<company_UUID> with required "team_lead" and "new team uuid"  
# without jwt token  
![3](https://user-images.githubusercontent.com/72104547/192118446-030ba30e-9a07-4528-9b03-3373114e00b4.png)  
# jwt authenticated screenshot  
![4](https://user-images.githubusercontent.com/72104547/192118455-54cb5adc-57ba-4431-88b5-edcc28265ee0.png)  
this entry was added successfully  
# 3.Get Company object from ID  
GET method at http://127.0.0.1:8000/Company/<company UUID>  with authentication headers  
# without jwt token  
![5](https://user-images.githubusercontent.com/72104547/192118561-0760a454-3893-4926-8223-597a0939e8a4.png)  
# with jwt  
![6](https://user-images.githubusercontent.com/72104547/192118573-3e86db4d-9370-441c-b01a-b093d8a464e7.png)  
# 4.Search company by name  
GET method at http://127.0.0.1:8000/CompanySearch/<company_name>  
# case a: when company searched for, does not exist in database  
![7](https://user-images.githubusercontent.com/72104547/192118644-ea347de6-ff2d-4ddc-ba01-451638cef1f6.png)  
# case b: when company searched for, exists  
![8](https://user-images.githubusercontent.com/72104547/192118650-24d07786-c42f-49b1-89b9-c73d1806fe0f.png)  
# 5.Get All teams (Return all teams as an array grouped within company object)  
GET request at http://localhost:8000/GetTeams/  
# without jwt  
![9](https://user-images.githubusercontent.com/72104547/192118721-4a6708b4-96a1-4857-ae17-30cee5545ff2.png)  
# with jwt  
![10](https://user-images.githubusercontent.com/72104547/192118725-269b4e00-0dc6-45b4-8f4e-e78696fcde56.png)  
# jwt details :
the used simple-jwt expires after 15 minutes by default, valid duration can be changed by editing settings.py file in main project  
# api for new jwt after expiration  
# POST request at http://127.0.0.1:8000/api/token/ with login password credentials of valid users ( existing )  
![11](https://user-images.githubusercontent.com/72104547/192119016-53bfc929-de30-4679-a143-10903399b219.jpg)


