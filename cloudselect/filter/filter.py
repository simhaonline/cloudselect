# Copyright 2019 Alexey Aksenov and individual contributors
# See the LICENSE.txt file at the top-level directory of this distribution.
#
# Licensed under the MIT license
# <LICENSE-MIT or http://opensource.org/licenses/MIT>
# This file may not be copied, modified, or distributed
# except according to those terms.
import dependency_injector.providers as providers

from cloudselect import Container


class FilterService(object):
    def run(self, service, metadata):
        return None

    def config(self):
        return Container.config().get("filter", {})


class FilterServiceProvider(providers.Singleton):

    provided_type = FilterService
