# FreelanceCove
### The freelance site for data scientists

# URL Enpoints
/  
/intermediate  
/freelance/sign-up  
/freelance/login  
/freelance/verify_signup  
/freelance/verify_login  
/frelance/home  
/job_detail/<int:job_id>  
/hiring/sign-up  
/hiring/login  
/hiring/verify_signup  
/hiring/home  
/hiring/available_freelancers  
/hiring/freelancer_details/<int:freelancer_id>  
/hiring/create_job  
/hiring/register  
  
1.**`[GET] /`**  
Loads the landing page

*Request*
- Method: `GET`
- Endpoint: `/`

- Compulsory request parameters - None
- Browser-based endpoint - True  

2.**`[GET] /intermediate`**  
Loads the lounge. An intermediary page for choosing whether you want to register as a freelancer or a hirer

*Request*
- Method: `GET`
- Endpoint: `/intermediate`

- Compulsory request parameters - None
- Browser-based endpoint - True  

3.**`[GET] /freelancer/sign-up`**  
Loads the freelancersign-up page

*Request*
- Method: `GET`
- Endpoint: `/freelance/sign-up`

- Compulsory request parameters - None
- Browser-based endpoint - True  

4.**`[GET] /freelance/login`**  
Loads Freelancer login page

*Request*
- Method: `GET`
- Endpoint: `/freelance/login`

- Compulsory request parameters - None
- Browser-based endpoint - True  

5.**`[GET]/freelance/home`**  
Retrieves all availalbale jobs from the database  

*Request*
- Method: `GET`
- Endpoint: `/freelance/home`

- Compulsory request parameters - None
- Browser-based endpoint - True  

6.**`[POST]/freelance/verify_sign-up`**  
Verifies that the logging in client is a non-existent user then registers the user and the credentials in the database.  

*Request*
- Method: `POST`
- Endpoint: `/freelance/verify_sign-up`

- Compulsory request parameters - None (Mandatory fields to be passed from '/freelance/sign-up' endpoint)
- Browser-based endpoint - False  

7.**`[POST]/freelance/verify_login`**  
Confirms logging in client is an existing user and password is correct

*Request*
- Method: `POST`
- Endpoint: `/freelance/verify_login`

- Compulsory request parameters - None
- Browser-based endpoint - False  (Mandatory fields to be passed from 'freelance/login' endpoint)