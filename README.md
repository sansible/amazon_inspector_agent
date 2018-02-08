# amazon_inspector_agent

Master: [![Build Status](https://travis-ci.org/sansible/amazon_inspector_agent.svg?branch=master)](https://travis-ci.org/sansible/amazon_inspector_agent)
Develop: [![Build Status](https://travis-ci.org/sansible/amazon_inspector_agent.svg?branch=develop)](https://travis-ci.org/sansible/amazon_inspector_agent)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This role downloads and installs[Amazon Inspector Agent](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_agents.html)
on supported GNU/Linux systems.  No parameters are required, but the following are supported:

| parameter | default | comments |
|---|---|---|
| sansible_amazon_inspector_agent_url | https://d1wk0tztpsntt1.cloudfront.net/linux/latest/install | URL from which to download the installation script |
| sansible_amazon_inspector_agent_dest | /tmp/amazon_inspector_agent | Path for the installation script |
| sansible_amazon_inspector_agent_enabled | yes | Whether the agent should be started automatically at boot (yes/no) |
| sansible_amazon_inspector_agent_state | started | The state of the agent after installation (started/stopped)  |
| sansible_amazon_inspector_agent_download_only | no | Download only, skip installation and configuration (yes/no) |


## Installation and Dependencies

To install run `ansible-galaxy install sansible.amazon_inspector_agent` or add this to your
`roles.yml`.

```YAML
- name: sansible.amazon_inspector_agent
  version: v1.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`


## Tags

This role uses tags: **build** and **configure**

* `build` - Downloads and installs Amazon Inspector Agent
* `configure` - Configures the status and autostart of Amazon Inspector Agent


## Examples

Simply include the role in your playbook

```YAML
- name: Install and configure Amazon Inspector Agent
  hosts: "somehost"

  roles:
    - role: sansible.amazon_inspector_agent
```
