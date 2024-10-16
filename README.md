# FreelanceCove
### The freelance site for data scientists

# URL Enpoints
/  
/intermediate  
/freelance/sign-up  
/freelance/login  
/freelance/verify_signup  
/freelance/verify_login  
/frelance/home - available jobs  
/job_detail/<int:job_id>  
/hiring/sign-up  
/hiring/login  
/hiring/verify_signup  
/hiring/home  
/hiring/available_freelancers  
/hiring/freelancer_details/<int:freelancer_id>  
/hiring/create_job  
/hiring/register  

**`[GET] /`**
Loads the landing page

*Request*
- Method: `GET`
- Endpoint: `/`

- Compulsory request parameters - None

**`[GET] /intermediate`**
Retrieves the lounge. An intermediary page for choosing whether you want to register as a freelancer or a hirer

*Request*
- Method: `GET`
- Endpoint: `/intermediate`

- Compulsory request parameters - None