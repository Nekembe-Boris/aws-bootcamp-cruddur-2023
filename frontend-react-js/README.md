### Create a virtual environment
```virtualenv --no-site-packages virenv```  

### Activate the virtual environment
```source virenv/bin/activate```

### Install nodeenv. It’s a tool to create isolated node.js environments
```pip install nodeenv```

### Add a node.js virtual environment to the existing environment that will also give you the npm package manager
```nodeenv -p```

### Install the create-react-app package using the npm package manager from node.js and create a new react app
```npm init react-app  Cruddur```
