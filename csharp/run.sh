function clean() {
    rm *.dll
    rm *.exe
    rm *.xml
}

function compile_testdll {
    mcs Demo.cs -target:library
    mcs DemoTest.cs -reference:nunit.framework.dll -reference:Demo.dll -target:library
}

function build {
    mcs Demo.cs
}

function ut {
        compile_testdll && \
        nunit-console2 DemoTest.dll
}

function usage {
  printf "
options:
       b: Build
      ut: Run Unit Test only
       c: Clean

"
}

function main {
  case $1 in
    b) build ;;
    ut) ut ;;
    c) clean ;;
    *) usage;;
  esac
}

main $@