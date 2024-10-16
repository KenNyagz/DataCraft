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
Loads the freelancer sign-up form

*Request*
- Method: `GET`
- Endpoint: `/freelance/sign-up`

- Compulsory request parameters - None
- Browser-based endpoint - True  

4.**`[GET] /freelance/login`**  
Loads Freelancer login form

*Request*
- Method: `GET`
- Endpoint: `/freelance/login`

- Compulsory request parameters - None
- Browser-based endpoint - True  

5.**`[POST]/freelance/verify_sign-up`**  
Verifies that the signing up client is a non-existent user then registers the user and the credentials in the database.  

*Request*
- Method: `POST`
- Endpoint: `/freelance/verify_sign-up`

- Compulsory request parameters - None (Mandatory fields to be passed from '/freelance/sign-up' page)
- Browser-based endpoint - False  

6.**`[POST]/freelance/verify_login`**  
Confirms logging in client is an existing user and password is correct

*Request*
- Method: `POST`
- Endpoint: `/freelance/verify_login`

- Compulsory request parameters - None (Mandatory fields to be passed from 'freelance/login' page)
- Browser-based endpoint - False  

7.**`[GET]/freelance/home`**  
Retrieves all availalbale jobs from the database and displays them  

*Request*
- Method: `GET`
- Endpoint: `/freelance/home`

- Compulsory request parameters - None
- Browser-based endpoint - True  

8.**`[GET]/freelance/job_detail/<int: job_id>`**  
Retrieves details pertaining specified job and fills template then sends it to the frontend to be rendered

*Request*
- Method: 'GET'
- Endpoint: `/freelance/job_detail/<int: job_id>

- Compulsory request parameters - None (Mandatory fields to be passed from 'freelance/login' page)
- Browser-based endpoint - True  

9.**`[GET]/hiring/sign-up`**  
Loads the hirer sign-up form  

*Request*
- Method: `GET`
- Endpoint: `/freelance/sign-up`

- Compulsory request parameters - None
- Browser-based endpoint - True  

10.**`[GET]/hiring/login`**  
Loads the hirer login form  

*Request*
- Method: `GET`
- Endpoint: `/freelance/login`

- Compulsory request parameters - None
- Browser-based endpoint - True  

11.**`[POST]/hiring/verify_signup`**  
Loads the hirer sign-up page  

*Request*
- Method: `GET`
- Endpoint: `/freelance/sign-up`

- Compulsory request parameters - None
- Browser-based endpoint - True  
[post]