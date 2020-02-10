## Purpose

We have to jump between nodes quickly. There is a list of cloud accounts. Each account has multiple regions. Some nodes are publicity available, some of them not. Dozen of nodes sit behind bastion hosts. And few of them sit behind a group of jump points. And they all have different SSH keys.

There is a `~/.ssh/config`, but it is not enough because of the dynamic nature of the cloud. It is too clumsy. It is not suitable for cases when IP addresses are changing instantly, and instances are creating and destroying in minutes.

I tried to structure that hell with shell scripts, but the shell is not enough. I believe that tools like *C*/*C++*/*Java*/*Node.JS*/*Go*?/*Rust* are too heavy for this case. Python is the exact thing. I like to have a dynamic and lightweight solution. Cloud Select is fast enough to go through thousands of nodes. Maybe if my scope will be higher, then I'll create something other.

It is useful for diving inside geo-distributed onion enterprise environments with weird security settings.

## Implementation

CloudSelect retrieves node list from the cloud, passes that list to FZF, adds some useful information to selected nodes (like jump hosts, `sudo -i` command, etc...), and returns JSON dictionary that could be used by other programs. CloudSelect is a team player in a shell environment. We can automatically open multiple interactive SSH sessions and provide passwords to `sudo -i` under TMUX environment.

## Demo

[![demo](https://raw.githubusercontent.com/ezh/cloudselect/master/docs/demo/2019-12-11_23-04-56%20cloudselect%20demo.gif)](https://github.com/ezh/cloudselect/tree/master/docs/demo)

The tool is:

1.  connecting to bastion host with public IP 54.171.154.230
2.  using locally stored key on bastion because the usage of ssh-agent is restricted by security team ?lol? and sshd settings are `AllowTcpForwarding no`, `GatewayPorts no`
3.  jumping to 4 EC2 web instances in development environment that located in private subnet 172.30.x.x
4.  running `sudo -i` at startup
5.  entering `sudo` password 12345678

&nbsp; *And after that, we have four ready to use interactive sessions in our terminal...*

You may find a demo files in <a href="https://github.com/ezh/cloudselect/tree/master/docs/demo" target="_blank">docs/demo</a> directory.

## Basic usage

-   Connect to a single known_hosts server
-   Connect to a single EC2 AWS instance

P.S. To be exact, *connect* or *execute* command or whatever you like

## Advanced usage

-   Connect to multiple known_hosts servers, run `sudo -i` command at startup and enter `sudo` password
-   Connect to multiple EC2 AWS instances, run `sudo -i` command at startup and enter `sudo` password
-   Connect to multiple EC2 AWS instances through a *bastion* host, run `sudo -i` command at startup and enter `sudo` password

P.S. To be exact, *connect* or *execute* command or whatever you like

## Features

:rocket: We may use jump hosts even if jump host hasn't been configured to allow remote port forwarding and we have the following settings in sshd_config:

        AllowTcpForwarding no
        GatewayPorts no