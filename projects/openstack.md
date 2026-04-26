---
name: OpenStack
url: https://opendev.org/openstack
license: Apache-2.0
language: Python
difficulty: intermediate
status: active
---

## What it does

Full IaaS cloud platform: compute (Nova), networking (Neutron), storage (Cinder/Swift), identity (Keystone), orchestration (Heat), containers (Magnum), bare metal (Ironic). Powers private clouds at telcos, governments, and research institutions worldwide.

## Why contribute

- Python at scale: real distributed systems, async message queuing (RabbitMQ), REST APIs
- Teaches every layer of cloud: from API surface down to hypervisor calls
- Governed by OpenInfra Foundation — very structured mentorship program
- Code review through Gerrit — teaches rigorous review culture

## Dev environment setup

```bash
# DevStack is the fastest way to get a running OpenStack
git clone https://opendev.org/openstack/devstack
cd devstack
cp samples/local.conf local.conf
# Edit local.conf to set passwords, enable services
./stack.sh
# Takes ~30 min; gives you Horizon UI at http://localhost/dashboard
```

## Where to find good first issues

- StoryBoard (OpenStack bug tracker): https://storyboard.openstack.org
- Filter by project + `low-hanging-fruit` tag
- Easy start: unit test improvements, documentation patches

## Community

- Mailing list: openstack-discuss@lists.openstack.org
- IRC: #openstack-dev on OFTC
- Weekly project meetings: https://meetings.opendev.org/
- Contributor guide: https://docs.openstack.org/contributors/

## Learning resources

- Contributor guide: https://docs.openstack.org/contributors/
- Architecture: https://docs.openstack.org/arch-design/
- Start with Nova: read `nova/compute/manager.py` — the heart of VM scheduling
- Recommended sequence: Keystone → Nova → Neutron → pick a specialty
