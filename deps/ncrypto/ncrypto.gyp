{
  'variables': {
    'ncrypto_sources': [
      'engine.cc',
      'dh-primes.h',
      'ncrypto.cc',
      'ncrypto.h',
    ],
  },
  'targets': [
    {
      'target_name': 'ncrypto',
      'type': 'static_library',
      'include_dirs': ['.'],
      'direct_dependent_settings': {
        'include_dirs': ['.'],
      },
      # nodejs-mobile patch: add C++20 standard
      "cflags_cc": ["-std=c++20"],  
      'sources': [ '<@(ncrypto_sources)' ],
      'conditions': [
        ['node_shared_openssl=="false"', {
          'dependencies': [
            '../openssl/openssl.gyp:openssl'
          ]
        }],
      ]
    },
  ]
}
