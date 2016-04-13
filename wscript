def options(opt):
    opt.load('compiler_cxx')

def configure(conf):
    conf.load('compiler_cxx')

def build(bld):
    source = \
    [
        'googletest/src/gtest-all.cc',
        'googlemock/src/gmock-all.cc'
    ]

    includes = \
    [
        'googletest',
        'googletest/include',
        'googlemock',
        'googlemock/include'
    ]

    if not bld.variant or bld.variant == 'test':
        bld.stlib(source = source,
                  includes = includes,
                  target = 'gtest')
