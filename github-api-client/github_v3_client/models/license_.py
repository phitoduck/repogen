from typing import Any, Dict, List, Optional, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="License")


@attr.s(auto_attribs=True)
class License:
    """License

    Attributes:
        key (str):  Example: mit.
        name (str):  Example: MIT License.
        node_id (str):  Example: MDc6TGljZW5zZW1pdA==.
        html_url (str):  Example: http://choosealicense.com/licenses/mit/.
        description (str):  Example: A permissive license that is short and to the point. It lets people do anything
            with your code with proper attribution and without warranty..
        implementation (str):  Example: Create a text file (typically named LICENSE or LICENSE.txt) in the root of your
            source code and copy the text of the license into the file. Replace [year] with the current year and [fullname]
            with the name (or names) of the copyright holders..
        permissions (List[str]):  Example: ['commercial-use', 'modifications', 'distribution', 'sublicense', 'private-
            use'].
        conditions (List[str]):  Example: ['include-copyright'].
        limitations (List[str]):  Example: ['no-liability'].
        body (str):  Example:

            The MIT License (MIT)

            Copyright (c) [year] [fullname]

            Permission is hereby granted, free of charge, to any person obtaining a copy
            of this software and associated documentation files (the "Software"), to deal
            in the Software without restriction, including without limitation the rights
            to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
            copies of the Software, and to permit persons to whom the Software is
            furnished to do so, subject to the following conditions:

            The above copyright notice and this permission notice shall be included in all
            copies or substantial portions of the Software.

            THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
            IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
            FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
            AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
            LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
            OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
            SOFTWARE.
            .
        featured (bool):  Example: True.
        spdx_id (Optional[str]):  Example: MIT.
        url (Optional[str]):  Example: https://api.github.com/licenses/mit.
    """

    key: str
    name: str
    node_id: str
    html_url: str
    description: str
    implementation: str
    permissions: List[str]
    conditions: List[str]
    limitations: List[str]
    body: str
    featured: bool
    spdx_id: Optional[str]
    url: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        name = self.name
        node_id = self.node_id
        html_url = self.html_url
        description = self.description
        implementation = self.implementation
        permissions = self.permissions

        conditions = self.conditions

        limitations = self.limitations

        body = self.body
        featured = self.featured
        spdx_id = self.spdx_id
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "node_id": node_id,
                "html_url": html_url,
                "description": description,
                "implementation": implementation,
                "permissions": permissions,
                "conditions": conditions,
                "limitations": limitations,
                "body": body,
                "featured": featured,
                "spdx_id": spdx_id,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        name = d.pop("name")

        node_id = d.pop("node_id")

        html_url = d.pop("html_url")

        description = d.pop("description")

        implementation = d.pop("implementation")

        permissions = cast(List[str], d.pop("permissions"))

        conditions = cast(List[str], d.pop("conditions"))

        limitations = cast(List[str], d.pop("limitations"))

        body = d.pop("body")

        featured = d.pop("featured")

        spdx_id = d.pop("spdx_id")

        url = d.pop("url")

        license_ = cls(
            key=key,
            name=name,
            node_id=node_id,
            html_url=html_url,
            description=description,
            implementation=implementation,
            permissions=permissions,
            conditions=conditions,
            limitations=limitations,
            body=body,
            featured=featured,
            spdx_id=spdx_id,
            url=url,
        )

        license_.additional_properties = d
        return license_

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
