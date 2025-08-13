{
  'target_defaults': {
    'conditions': [
      # Override common.gypi config to use C++20 for Node.js core only.
      ['OS in "linux freebsd openbsd solaris android aix os400 cloudabi"', {
        # nodejs-mobile patch: add C++17 standard. see deps/v8/src/handles.h:141
        'cflags_cc': ['-std=gnu++17'],
        'cflags_cc!': ['-std=gnu++20'],
      }],
      ['OS=="mac" and clang==1', {
        'xcode_settings': {
          'CLANG_CXX_LANGUAGE_STANDARD': 'gnu++20',  # -std=gnu++20
        },
      }],
    ],
  },
}
