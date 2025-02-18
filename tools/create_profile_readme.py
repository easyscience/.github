import yaml
from typing import Dict


def read_yaml(file_path: str) -> Dict:
    """
    Reads a YAML file and returns its content as a dictionary.
    :param file_path: Path to the YAML file.
    :return: Parsed YAML content as a dictionary.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)


def write_markdown(file_path: str, content: str) -> None:
    """
    Writes the generated Markdown content to a file.
    :param file_path: Path to the Markdown file.
    :param content: Markdown content to write.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def generate_project_logo(project_name: str) -> str:
    """
    Generates an HTML block for a project's logo using branding assets.
    :param project_name: Name of the project.
    :return: HTML picture element containing light and dark mode images.
    """
    project_slug = project_name.lower()
    logos_url = f"https://raw.githubusercontent.com/easyscience/assets-branding/refs/heads/master/{project_slug}/logos"
    return (f"<picture>"
            f"<source media='(prefers-color-scheme: light)' srcset='{logos_url}/light.svg'>"
            f"<source media='(prefers-color-scheme: dark)' srcset='{logos_url}/dark.svg'>"
            f"<img src='{logos_url}/light.svg' height='37px' alt='{project_name}'>"
            f"</picture>")


def generate_icon(icon_name: str) -> str:
    """
    Generates an HTML image tag for an icon using FontAwesome assets.
    :param icon_name: Name of the FontAwesome icon.
    :return: HTML image element containing the icon.
    """
    icons_url = f"https://raw.githubusercontent.com/easyscience/assets-branding/refs/heads/master/fontawesome"
    return (f"<picture>"
            f"<source media='(prefers-color-scheme: light)' srcset='{icons_url}/{icon_name}_light.svg'>"
            f"<source media='(prefers-color-scheme: dark)' srcset='{icons_url}/{icon_name}_dark.svg'>"
            f"<img src='{icons_url}/{icon_name}_light.svg' height='20px'>"
            f"</picture>")


def generate_repository_links(data: Dict) -> str:
    """
    Generates a Markdown section with repository links for domain-specific projects and core modules.
    :param data: Dictionary containing project information from YAML.
    :return: Markdown-formatted repository links.
    """
    org_url = 'https://github.com/easyscience'
    links_md = "\n<!---Domain-Specific Projects--->\n"

    for project in data['domain-specific-projects']:
        for repo_type, repo_name in project['repos'].items():
            links_md += f"[{repo_name}]: {org_url}/{repo_name}\n"

    links_md += "\n<!---Core Framework Modules--->\n"
    for module in data['core-framework-modules']:
        links_md += f"[{module['repo']}]: {org_url}/{module['repo']}\n"

    return links_md


def generate_markdown(data: Dict) -> str:
    """
    Generates the full Markdown content for domain-specific projects and core framework modules.
    :param data: Dictionary containing project details from YAML.
    :return: Markdown-formatted string.
    """
    # Domain-Specific Projects Table
    markdown_output = "### Domain-Specific Projects\n\nThese projects focus on different scientific techniques for data analysis and reduction.\n\n"
    markdown_output += (f"| {generate_icon('fa-folder')}<br/>Project | "
                        f"{generate_icon('fa-tag')}<br/>Tag | "
                        f"{generate_icon('fa-circle-info')}<br/>Description | "
                        f"{generate_icon('fa-house')}<br/>Home | "
                        f"{generate_icon('fa-box')}<br/>Library | "
                        f"{generate_icon('fa-window-maximize')}<br/>Application |\n")
    markdown_output += "|-|-|-|-|-|-|\n"

    for project in data['domain-specific-projects']:
        logo = generate_project_logo(project['name'])
        shortcut = project['shortcut']
        description = f"{project['description']['main']}<br/>`{project['description']['type']}`"

        project_home = f"[{project['repos'].get('project', '')}]" if 'project' in project['repos'] else ""
        python_lib = f"[{project['repos'].get('lib', '')}]" if 'lib' in project['repos'] else ""
        desktop_app = f"[{project['repos'].get('app', '')}]" if 'app' in project['repos'] else ""

        markdown_output += f"| {logo} | {shortcut} | {description} | {project_home} | {python_lib} | {desktop_app} |\n"

    # Core Framework Modules Table
    markdown_output += "\n### Core Framework Modules\n\nThese are essential building blocks that support the domain-specific projects.\n\n"
    markdown_output += (f"| {generate_icon('fa-folder')}<br/>Project | "
                        f"{generate_icon('fa-tag')}<br/>Tag | "
                        f"{generate_icon('fa-circle-info')}<br/>Description | "
                        f"{generate_icon('fa-box')}<br/>Library |\n")
    markdown_output += "|-|-|-|-|\n"

    for module in data['core-framework-modules']:
        logo = generate_project_logo(module['name'])
        shortcut = module['shortcut']
        description = f"{module['description']['main']}<br/>`{module['description']['type']}`"
        repo = f"[{module['repo']}]"

        markdown_output += f"| {logo} | {shortcut} | {description} | {repo} |\n"

    # Append Link to the main README.md
    markdown_output += "\n\n More details on creating new projects within the **EasyScience** organization can be found [here](https://github.com/easyscience/.github/blob/master/README.md)."

    # Append Repository Links
    markdown_output += "\n\n" + generate_repository_links(data)

    # TEMPORARY FIX: Change some project urls
    urls = {
        "https://github.com/easyscience/diffraction-lib": "https://github.com/easyscience/EasyDiffractionLib",
        "https://github.com/easyscience/diffraction-app": "https://github.com/easyscience/EasyDiffractionApp",
        "https://github.com/easyscience/diffraction": "https://github.com/easyscience/EasyDiffraction",
        "https://github.com/easyscience/reflectometry-lib": "https://github.com/easyscience/EasyReflectometryLib",
        "https://github.com/easyscience/reflectometry-app": "https://github.com/easyscience/EasyReflectometryApp",
        "https://github.com/easyscience/reflectometry": "https://github.com/easyscience/EasyReflectometry",
        "https://github.com/easyscience/crystallography": "https://github.com/easyscience/EasyCrystallography",
        "https://github.com/easyscience/guilib": "https://github.com/easyscience/EasyApp",
    }
    for old_url, new_url in urls.items():
        markdown_output = markdown_output.replace(old_url, new_url)

    return markdown_output


if __name__ == "__main__":
    yaml_file_path = "profile/README.yaml"  # Path to input YAML file
    markdown_file_path = "profile/README.md"  # Path to output Markdown file

    project_data = read_yaml(yaml_file_path)
    markdown_content = generate_markdown(project_data)
    write_markdown(markdown_file_path, markdown_content)

    print("Markdown file has been successfully generated.")
