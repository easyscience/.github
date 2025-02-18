<p>
  <picture>
    <!-- Light mode -->
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/easyscience/assets-branding/refs/heads/master/easyscience-org/logos/light.svg">
    <!-- Dark mode -->
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/easyscience/assets-branding/refs/heads/master/easyscience-org/logos/dark.svg">
    <!-- Default -->
    <img src="https://raw.githubusercontent.com/easyscience/assets-branding/refs/heads/master/easyscience-org/logos/light.svg" height="37px" alt="EasyScience">
  </picture>
</p>

**EasyScience** is a versatile data analysis framework designed to streamline the journey from **data collection to publication**. It provides:
- **Powerful back-end tools**: Core functionality through Python libraries.
- **Efficient front-end modules**: QML components for developing desktop applications with ease.

## 1. Set Up GitHub Access
*(Required only if GitHub access has not been set up before.)*

GitHub access is managed via **Personal Access Tokens (PATs)**:

### 1.1 Generate a Personal Access Token (PAT)
1. Go to **GitHub → Settings → Developer Settings → Personal Access Tokens**.
2. Click **"Generate new token"**.
3. Select:
   - ✅ **repo** → Full control of repositories.
   - ✅ **workflow** → Access GitHub Actions *(optional)*.
4. Click **"Generate token"** and copy it.

### 1.2 Using PAT
You can now interact with GitHub using:
- **Terminal** *(Recommended for advanced users).*
- **GUI tools** *(e.g., GitKraken for an intuitive interface).*

## 2. Define the Project in the Organization Profile
Each project should be **registered** in the EasyScience organization profile.

### 2.1 Add Project Definition
Edit [README.yaml](https://github.com/easyscience/.github/blob/master/profile/README.yaml) under `domain-specific-projects`.  

### 2.2 Include the following details:
- **name** → The project name, prefixed with **Easy** (e.g., *EasyDiffraction*).
- **shortcut** → A short, two-letter abbreviation (e.g., *ED*).
- **description**:
  - **main** → A brief project description (e.g. *Diffraction*).
  - **type** → Type of project (e.g., *data analysis*, *visualization*).
- **repos**:
  - **home** → Home repository name (e.g., *diffraction*).
  - **lib** → Library repository name *(if applicable)*.
  - **app** → Application repository name *(if applicable)*.

### 2.3 Example (EasyDiffraction)
```yaml
  - name: EasyDiffraction
    shortcut: ED
    description:
      main: Diffraction
      type: data analysis
    repos:
      home: diffraction
      lib: diffraction-lib
      app: diffraction-app
```

## 3. Create Repositories Using Templates
EasyScience provides predefined **Copier templates** for new repositories:

| **Template**   | **Purpose**                           | **Repository**                                                                  |
|----------------|---------------------------------------|---------------------------------------------------------------------------------|
| `project-base` | Base project template                 | [templates-project-base](https://github.com/easyscience/templates-project-base) |
| `project-home` | Home project repository               | [templates-project-home](https://github.com/easyscience/templates-project-home) |
| `project-lib`  | Python package repository             | [templates-project-lib](https://github.com/easyscience/templates-project-lib)   |
| `project-app`  | Qt QML desktop application repository | [templates-project-app](https://github.com/easyscience/templates-project-app)   |

### 3.1 Create a Repository on GitHub
Here is an example for creating a new repository `superduper-lib` which will be a Python 
library for the project `SuperDuper`. Creating a new repository `superduper` (project home) or `superduper-app` 
(desktop app) could be done in a similar way.

Create a project home repository:

1. Navigate to **GitHub** → **Create New Repository**.
2. **Repository template:** No template *(we will use Copier instead)*.
3. **Enter the repository name**, e.g., `superduper-lib`.
4. Add a description based on the [README.yaml](https://github.com/easyscience/.github/blob/master/profile/README.yaml) difinition from above, e.g., Diffraction data analysis.
5. **Set repository visibility** to **Public**.
6. **DO NOT initialize** with a README, `.gitignore`, or license *(Copier handles these)*.
7. Click **"Create repository"**.

### 3.2 Clone the Repository
```bash
git clone https://github.com/easyscience/superduper-lib.git
cd superduper-lib
```

*(Alternatively, use GitKraken or another Git client.)*

### 3.3 Set Up a Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3.4 Install & Run Copier
Install Copier if not already installed:
```bash
pip install copier
```
Generate the project structure:
```bash
copier copy gh:easyscience/templates-project-base ./
```
*(Follow interactive prompts to configure the project.)*

### 3.5 Extend with Additional Templates
To add **Python library files**:
```bash
copier copy gh:easyscience/templates-project-lib ./ --data-file .copier-answers.project.yml
```

## 4. Push Changes to GitHub
After generating the project structure, **commit and push the changes**:

```bash
cd superduper-lib
git add -A
git commit -m "Initial project setup using Copier templates"
git push origin master
```
*(Alternatively, use a GUI client like GitKraken.)*

## 5. Repository Configuration
Some settings must be configured manually:
- **Add repository secrets** *(e.g., API keys, deployment keys)*.
- **Configure branch protection & access control**.

## 6. Updating the Repository with Template Changes
When the template is updated in **templates-project-base** and/or **templates-project-lib**, apply changes using:

### 6.1 Update Base Project Definition Templates
```bash
cd superduper-lib
copier update --answers-file=.copier-answers.project-base.yml
```
Push changes:
```bash
git add -A
git commit -m "Updated project structure with latest template"
git push origin master
```

### 6.2 Update Library-Specific Files
```bash
copier update --answers-file=.copier-answers.project-lib.yml --data-file .copier-answers.project.yml
```
Push changes:
```bash
git add -A
git commit -m "Updated Python library structure with latest template"
git push origin master
```

*(If conflicts arise, Copier will prompt you to review them.)*
