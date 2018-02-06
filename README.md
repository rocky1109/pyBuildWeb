# pyBuildWeb
A python sdk to access buildweb APIs.

## Installation

Clone the project in your local directory.
```
git clone https://github.com/rocky1109/pyBuildWeb.git
cd pyBuildWeb
```

Now install/build it using **setup.py** file as
```
python setup.py install
```

## Example
```python
>> from pyBuildWeb import BuildWeb, Build
>> from pprint import pprint
>> 
>> build = Build(id="123456")
>> pprint(build.deliverables, indent=4)
[   <Deliverable-metadata.xml.gz(4913138)>,
    <Deliverable-index.html(4913138)>,
    <Deliverable-modules.zip(4913138)>]
>> 
>> # To download the deliverables from the build
>> build.download_deliverables(at_path="/path/where/deliverables/should/download")
>> 
>> # To download a particular deliverable
>> build.deliverables[-2].download(at_path="/path/where/deliverables/should/download")
>> 
>> buildweb = BuildWeb(product="nsx-transformers", buildtype="ob", state="succeeded")
>> pprint(buildweb.builds, indent=4)
[   <Build-6789659>, 
    <Build-6790880>, 
    <Build-6794303>, 
    <Build-6794668>]
>> 
>> isinstance(buildweb.builds[0], Build)
```
