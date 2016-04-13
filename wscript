def options(opt):
    opt.load('compiler_cxx')

def configure(conf):
    conf.load('compiler_cxx')

def build(bld):
    bld.stlib(source=\
              [
                'googletest/src/gtest-all.cc',
                'googlemock/src/gmock-all.cc'
              ],
              includes=\
              [
                'googletest',
                'googlemock',
                'googletest/include',
                'googlemock/include'
              ],
              target='gtest')
