# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from horizon import views
from horizon import tables
from openstack_dashboard.dashboards.mydashboard.userpanel import tables as project_tables
from docker import Client

class Image:
    def __init__(self,size,parentId,imageId,repoTags,virtualSize,created):
        self.id = imageId
        self.size = size
        self.parentId = parentId
        self.created = created
        self.imageId = imageId
        self.repoTags = repoTags
        self.virtualSize = virtualSize

class IndexView(tables.DataTableView):
    # A very simple class-based view...
    template_name = 'mydashboard/userpanel/index.html'
    table_class = project_tables.ImageDocker
    page_title = 'Image Docker'

    def get_data(self):
        # Add data to the context here...
        images =[]
        cli = Client(base_url='unix://var/run/docker.sock')
        imagess = cli.images()
        for image in imagess:
            repo = image['RepoTags']
            repoTags = repo[0]
            img = Image(image['Size'],image['ParentId'],image['Id'],repoTags,image['VirtualSize'],image['Created'])
            images.append(img)
        return images
