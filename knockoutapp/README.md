## About This Generator
This will get you up and running with a skeleton SPA using the [Durandal](http://durandaljs.com/) framework and pre-configured Gulp tasks.

###Language Support:
* JavaScript(ES5)
* TypeScript

###UI Options:
* [Normalize](https://necolas.github.io/normalize.css/)
* [Bootstrap](https://getbootstrap.com/)
* [Bootstrap Material Design](https://fezvrasta.github.io/bootstrap-material-design/#getting-started)
* [Font Awesome](https://fortawesome.github.io/Font-Awesome/)

###Planned Updates:
* Bower support
* JSPM
* Babel6



## Getting Started

### Environment Setup
Ensure that [NodeJS](http://nodejs.org/) is installed. This provides the platform on which the build tooling runs.
From the project folder, execute the following command:

  ```shell
  npm install
  ```
Ensure that [Gulp](http://gulpjs.com/) is installed globally. If you need to install it, use the following command:

  ```shell
  npm install -g gulp
  ```
  > **Note:** Gulp must be installed globally, but a local version will also be installed to ensure a compatible version is used for the project.

### Install Yeoman

This generator needs Yeoman to be installed.

```shell
npm install -g yo
```

### Install Generator

To install generator-durandal2 from npm, run:

```shell
npm install -g generator-durandal2
```

Then, initiate the generator:

```shell
yo durandal2
```

##Development

### Run the Application

> **Note:** If using TypeScript configuration, install necessary type definitions
```shell
typings install
```

```shell
gulp watch

```
Browse to [http://localhost:9000](http://localhost:9000) to see the app. You can make changes in the code found under `app` and the browser should auto-refresh itself as you save files.
> This template uses [BrowserSync](http://www.browsersync.io/) for automated page refreshes on code/markup changes concurrently across multiple browsers. If you prefer to disable the mirroring feature set the [ghostMode option](http://www.browsersync.io/docs/options/#option-ghostMode) to false



### Sub Generators

####ViewModel

You can create a viewmodel the following subgenerator.
You can choose between TypeScript or JavaScript. 

```shell
yo durandal2:viewmodel {name} {transpiler} (--transient)
```
> **Note:** Passing --transient will create a viewmodel with a transient lifecycle

## License

[MIT License](http://en.wikipedia.org/wiki/MIT_License)