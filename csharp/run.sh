function clean() {
    rm *.dll
    rm *.exe
    rm *.xml
}

function compile_testdll {
    mcs Demo2.cs -target:library
    mcs Demo2Test.cs -reference:nunit.framework.dll -reference:Demo2.dll -target:library
}

function build {
    mcs Demo2.cs
}

function ut {
        compile_testdll && \
        nunit-console2 Demo2Test.dll
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