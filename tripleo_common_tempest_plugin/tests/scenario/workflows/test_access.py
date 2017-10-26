# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from tempest.lib import decorators
from tempest import test

from tripleo_common_tempest_plugin.tests import base



class AccessWorkflowTestCase(test.BaseTestCase):

    @decorators.attr(type='openstack')
    @decorators.idempotent_id('2d9bf96a-2d1f-4c79-a44d-97208bd0e1a3')
    def test_noop(self):
        pass
