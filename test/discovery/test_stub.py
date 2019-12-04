# Copyright 2019 Alexey Aksenov and individual contributors
# See the LICENSE.txt file at the top-level directory of this distribution.
#
# Licensed under the MIT license
# <LICENSE-MIT or http://opensource.org/licenses/MIT>
# This file may not be copied, modified, or distributed
# except according to those terms.
from cloudselect import Container
from cloudselect.cloudselect import CloudSelect
from cloudselect.discovery import DiscoveryServiceProvider
from cloudselect.discovery.stub import Stub


def test_stub_discovery():
    cloud = CloudSelect()
    # Read shared part
    profile = cloud.read_configuration()
    args = cloud.parse_args([])
    cloud.fabric(profile, args)
    assert Container.discovery().__class__.__name__ == "Stub"
    assert Container.discovery().run() == []
    assert Container.discovery() == Container.discovery()


def test_stub_behaviour(mocker):
    cloud = CloudSelect()
    service_provider = cloud.plugin(
        "cloudselect.discovery.stub", DiscoveryServiceProvider
    )
    stub = service_provider()
    mocker.patch.object(Stub, "run")
    stub.run()
    Stub.run.assert_called_once_with()
