## Flask CI/CD Pipeline Documentation

### Tools Used

1. **Flask**: A lightweight Python web framework suitable for developing small to large scale web applications. Flask is chosen for its simplicity and ease of use for this basic todo app.
   
2. **GitHub Actions**: A CI/CD tool integrated directly into GitHub. It allows for automating software workflows, including testing and deployment, directly from your GitHub repository.
   
3. **AWS Elastic Beanstalk**: A cloud service that makes it easy to deploy, manage, and scale web applications and services developed with multiple languages, including Python. Elastic Beanstalk is chosen for its simplicity in deploying Flask applications and its scalability options.

### Pipeline Steps

#### 1. Setting Up the Flask Todo App

**Reason**: Flask is chosen due to its simplicity and flexibility. It provides the necessary features to create a basic todo application without being overly complex.

**Steps**:

- Task 1:Create a web application using FLask
This repo has been updated to work with `Python v3.9` and up.

### To clone this repo
git clone https://github.com/PRATIKNALAWADE/flask-cicd

### How To Run
1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:
```
$ .\env\Scripts\activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Finally start the web server:
```
$ (env) python app.py
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```

#### 2. Writing Unit Tests

**Reason**: Unit tests are essential to ensure the application works as expected and to catch any regressions in the codebase.

**Steps**:

- Write unit tests using Python's `unittest` framework or `pytest`.
- Test the Flask routes to ensure they handle CRUD operations correctly.
  
#### 3. Setting Up GitHub Actions Workflow

**Reason**: GitHub Actions allows automating the CI/CD process directly within the GitHub repository, making it easier to manage and maintain.

**Steps**:Task 3: Use GitHub Actions to set up a CI/CD pipeline that:
Runs the tests on every push to the repository.
Deploys the application to a free-tier cloud service 

Workflow code, refer to .github/workflows/main.yml

- Create a `.github/workflows/main.yml` file to define the workflow.
- Define jobs to install dependencies, run unit tests, and deploy the application.

#### 4. Configuring AWS Elastic Beanstalk Deployment

**Reason**: AWS Elastic Beanstalk simplifies the deployment process by handling the deployment details, such as provisioning resources and load balancing, allowing developers to focus on the application code.

**Steps**:

- Configure Elastic Beanstalk settings in the GitHub Actions workflow to deploy the Flask app.
- Set up AWS credentials and Elastic Beanstalk configuration files (`ebextensions`) for deployment.

### GitHub Actions Workflow Configuration (`.github/workflows/main.yml`)


### Reasons Behind Tool Choices

- **Flask**: Chosen for its simplicity, ease of use, and flexibility in building web applications. It allows for quick development of the todo app without unnecessary complexity.

- **GitHub Actions**: Integrated directly with GitHub, making it easy to set up CI/CD workflows without needing additional tools. It provides a seamless experience for developers, as everything is managed within the GitHub repository.

- **AWS Elastic Beanstalk**: Chosen for its ease of use in deploying and managing Flask applications. Elastic Beanstalk handles the infrastructure and scaling aspects, allowing developers to focus on the application code.

By using Flask for the web application, GitHub Actions for CI/CD, and AWS Elastic Beanstalk for deployment, we've created a streamlined development and deployment process. This setup allows for rapid development, testing, and deployment of the Flask todo app, ensuring a smooth user experience.


