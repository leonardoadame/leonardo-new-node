{
  'variables': {
    'openssl_sources': [
      'openssl/crypto/aes/aes_ecb.c',
      'openssl/crypto/aes/aes_misc.c',
      'openssl/crypto/bn/bn_add.c',
      'openssl/crypto/bn/bn_asm.c',
      'openssl/crypto/bn/bn_blind.c',
      'openssl/crypto/bn/bn_const.c',
      'openssl/crypto/bn/bn_conv.c',
      'openssl/crypto/bn/bn_ctx.c',
      'openssl/crypto/bn/bn_dh.c',
      'openssl/crypto/bn/bn_div.c',
      'openssl/crypto/bn/bn_exp.c',
      'openssl/crypto/bn/bn_exp2.c',
      'openssl/crypto/bn/bn_gcd.c',
      'openssl/crypto/bn/bn_gf2m.c',
      'openssl/crypto/bn/bn_intern.c',
      'openssl/crypto/bn/bn_kron.c',
      'openssl/crypto/bn/bn_lib.c',
      'openssl/crypto/bn/bn_mod.c',
      'openssl/crypto/bn/bn_mont.c',
      'openssl/crypto/bn/bn_mpi.c',
      'openssl/crypto/bn/bn_mul.c',
      'openssl/crypto/bn/bn_nist.c',
      'openssl/crypto/bn/bn_prime.c',
      'openssl/crypto/bn/bn_rand.c',
      'openssl/crypto/bn/bn_recp.c',
      'openssl/crypto/bn/bn_rsa_fips186_4.c',
      'openssl/crypto/bn/bn_shift.c',
      'openssl/crypto/bn/bn_sqr.c',
      'openssl/crypto/bn/bn_sqrt.c',
      'openssl/crypto/bn/bn_word.c',
      'openssl/crypto/bn/rsa_sup_mul.c',
      'openssl/crypto/bn/rsaz_exp.c',
      'openssl/crypto/bn/rsaz_exp_x2.c',
      'openssl/crypto/buffer/buffer.c',
      'openssl/crypto/cmac/cmac.c',
      'openssl/crypto/des/des_enc.c',
      'openssl/crypto/des/ecb3_enc.c',
      'openssl/crypto/des/fcrypt_b.c',
      'openssl/crypto/des/set_key.c',
      'openssl/crypto/dh/dh_backend.c',
      'openssl/crypto/dh/dh_check.c',
      'openssl/crypto/dh/dh_gen.c',
      'openssl/crypto/dh/dh_group_params.c',
      'openssl/crypto/dh/dh_kdf.c',
      'openssl/crypto/dh/dh_key.c',
      'openssl/crypto/dh/dh_lib.c',
      'openssl/crypto/dsa/dsa_backend.c',
      'openssl/crypto/dsa/dsa_check.c',
      'openssl/crypto/dsa/dsa_gen.c',
      'openssl/crypto/dsa/dsa_key.c',
      'openssl/crypto/dsa/dsa_lib.c',
      'openssl/crypto/dsa/dsa_ossl.c',
      'openssl/crypto/dsa/dsa_sign.c',
      'openssl/crypto/dsa/dsa_vrf.c',
      'openssl/crypto/ec/curve448/arch_32/f_impl32.c',
      'openssl/crypto/ec/curve448/arch_64/f_impl64.c',
      'openssl/crypto/ec/curve448/curve448.c',
      'openssl/crypto/ec/curve448/curve448_tables.c',
      'openssl/crypto/ec/curve448/eddsa.c',
      'openssl/crypto/ec/curve448/f_generic.c',
      'openssl/crypto/ec/curve448/scalar.c',
      'openssl/crypto/ec/curve25519.c',
      'openssl/crypto/ec/ec2_oct.c',
      'openssl/crypto/ec/ec2_smpl.c',
      'openssl/crypto/ec/ec_asn1.c',
      'openssl/crypto/ec/ec_backend.c',
      'openssl/crypto/ec/ec_check.c',
      'openssl/crypto/ec/ec_curve.c',
      'openssl/crypto/ec/ec_cvt.c',
      'openssl/crypto/ec/ec_key.c',
      'openssl/crypto/ec/ec_kmeth.c',
      'openssl/crypto/ec/ec_lib.c',
      'openssl/crypto/ec/ec_mult.c',
      'openssl/crypto/ec/ec_oct.c',
      'openssl/crypto/ec/ecdh_kdf.c',
      'openssl/crypto/ec/ecdh_ossl.c',
      'openssl/crypto/ec/ecdsa_ossl.c',
      'openssl/crypto/ec/ecdsa_sign.c',
      'openssl/crypto/ec/ecdsa_vrf.c',
      'openssl/crypto/ec/ecp_mont.c',
      'openssl/crypto/ec/ecp_nist.c',
      'openssl/crypto/ec/ecp_nistz256.c',
      'openssl/crypto/ec/ecp_oct.c',
      'openssl/crypto/ec/ecp_smpl.c',
      'openssl/crypto/ec/ecx_backend.c',
      'openssl/crypto/ec/ecx_key.c',
      'openssl/crypto/evp/asymcipher.c',
      'openssl/crypto/evp/dh_support.c',
      'openssl/crypto/evp/digest.c',
      'openssl/crypto/evp/ec_support.c',
      'openssl/crypto/evp/evp_enc.c',
      'openssl/crypto/evp/evp_fetch.c',
      'openssl/crypto/evp/evp_lib.c',
      'openssl/crypto/evp/evp_rand.c',
      'openssl/crypto/evp/evp_utils.c',
      'openssl/crypto/evp/exchange.c',
      'openssl/crypto/evp/kdf_lib.c',
      'openssl/crypto/evp/kdf_meth.c',
      'openssl/crypto/evp/kem.c',
      'openssl/crypto/evp/keymgmt_lib.c',
      'openssl/crypto/evp/keymgmt_meth.c',
      'openssl/crypto/evp/m_sigver.c',
      'openssl/crypto/evp/mac_lib.c',
      'openssl/crypto/evp/mac_meth.c',
      'openssl/crypto/evp/p_lib.c',
      'openssl/crypto/evp/pmeth_check.c',
      'openssl/crypto/evp/pmeth_gn.c',
      'openssl/crypto/evp/pmeth_lib.c',
      'openssl/crypto/evp/signature.c',
      'openssl/crypto/ffc/ffc_backend.c',
      'openssl/crypto/ffc/ffc_dh.c',
      'openssl/crypto/ffc/ffc_key_generate.c',
      'openssl/crypto/ffc/ffc_key_validate.c',
      'openssl/crypto/ffc/ffc_params.c',
      'openssl/crypto/ffc/ffc_params_generate.c',
      'openssl/crypto/ffc/ffc_params_validate.c',
      'openssl/crypto/hmac/hmac.c',
      'openssl/crypto/lhash/lhash.c',
      'openssl/crypto/asn1_dsa.c',
      'openssl/crypto/bsearch.c',
      'openssl/crypto/context.c',
      'openssl/crypto/core_algorithm.c',
      'openssl/crypto/core_fetch.c',
      'openssl/crypto/core_namemap.c',
      'openssl/crypto/cpuid.c',
      'openssl/crypto/cryptlib.c',
      'openssl/crypto/ctype.c',
      'openssl/crypto/der_writer.c',
      'openssl/crypto/ex_data.c',
      'openssl/crypto/initthread.c',
      'openssl/crypto/o_str.c',
      'openssl/crypto/packet.c',
      'openssl/crypto/param_build.c',
      'openssl/crypto/param_build_set.c',
      'openssl/crypto/params.c',
      'openssl/crypto/params_dup.c',
      'openssl/crypto/params_from_text.c',
      'openssl/crypto/provider_core.c',
      'openssl/crypto/provider_predefined.c',
      'openssl/crypto/self_test_core.c',
      'openssl/crypto/sparse_array.c',
      'openssl/crypto/threads_lib.c',
      'openssl/crypto/threads_none.c',
      'openssl/crypto/threads_pthread.c',
      'openssl/crypto/threads_win.c',
      'openssl/crypto/modes/cbc128.c',
      'openssl/crypto/modes/ccm128.c',
      'openssl/crypto/modes/cfb128.c',
      'openssl/crypto/modes/ctr128.c',
      'openssl/crypto/modes/gcm128.c',
      'openssl/crypto/modes/ofb128.c',
      'openssl/crypto/modes/wrap128.c',
      'openssl/crypto/modes/xts128.c',
      'openssl/crypto/property/defn_cache.c',
      'openssl/crypto/property/property.c',
      'openssl/crypto/property/property_parse.c',
      'openssl/crypto/property/property_query.c',
      'openssl/crypto/property/property_string.c',
      'openssl/crypto/rand/rand_lib.c',
      'openssl/crypto/rsa/rsa_acvp_test_params.c',
      'openssl/crypto/rsa/rsa_backend.c',
      'openssl/crypto/rsa/rsa_chk.c',
      'openssl/crypto/rsa/rsa_crpt.c',
      'openssl/crypto/rsa/rsa_gen.c',
      'openssl/crypto/rsa/rsa_lib.c',
      'openssl/crypto/rsa/rsa_mp_names.c',
      'openssl/crypto/rsa/rsa_none.c',
      'openssl/crypto/rsa/rsa_oaep.c',
      'openssl/crypto/rsa/rsa_ossl.c',
      'openssl/crypto/rsa/rsa_pk1.c',
      'openssl/crypto/rsa/rsa_pss.c',
      'openssl/crypto/rsa/rsa_schemes.c',
      'openssl/crypto/rsa/rsa_sign.c',
      'openssl/crypto/rsa/rsa_sp800_56b_check.c',
      'openssl/crypto/rsa/rsa_sp800_56b_gen.c',
      'openssl/crypto/rsa/rsa_x931.c',
      'openssl/crypto/sha/sha1dgst.c',
      'openssl/crypto/sha/sha256.c',
      'openssl/crypto/sha/sha3.c',
      'openssl/crypto/sha/sha512.c',
      'openssl/crypto/stack/stack.c',
      'openssl/providers/common/der/der_rsa_sig.c',
      'openssl/providers/common/bio_prov.c',
      'openssl/providers/common/capabilities.c',
      'openssl/providers/common/digest_to_nid.c',
      'openssl/providers/common/provider_seeding.c',
      'openssl/providers/common/provider_util.c',
      'openssl/providers/common/securitycheck.c',
      'openssl/providers/common/securitycheck_fips.c',
      'openssl/providers/fips/fipsprov.c',
      'openssl/providers/fips/self_test.c',
      'openssl/providers/fips/self_test_kats.c',
      'openssl/providers/implementations/asymciphers/rsa_enc.c',
      'openssl/providers/implementations/ciphers/cipher_aes.c',
      'openssl/providers/implementations/ciphers/cipher_aes_cbc_hmac_sha.c',
      'openssl/providers/implementations/ciphers/cipher_aes_cbc_hmac_sha1_hw.c',
      'openssl/providers/implementations/ciphers/cipher_aes_cbc_hmac_sha256_hw.c',
      'openssl/providers/implementations/ciphers/cipher_aes_ccm.c',
      'openssl/providers/implementations/ciphers/cipher_aes_ccm_hw.c',
      'openssl/providers/implementations/ciphers/cipher_aes_gcm.c',
      'openssl/providers/implementations/ciphers/cipher_aes_gcm_hw.c',
      'openssl/providers/implementations/ciphers/cipher_aes_hw.c',
      'openssl/providers/implementations/ciphers/cipher_aes_ocb.c',
      'openssl/providers/implementations/ciphers/cipher_aes_ocb_hw.c',
      'openssl/providers/implementations/ciphers/cipher_aes_wrp.c',
      'openssl/providers/implementations/ciphers/cipher_aes_xts.c',
      'openssl/providers/implementations/ciphers/cipher_aes_xts_fips.c',
      'openssl/providers/implementations/ciphers/cipher_aes_xts_hw.c',
      'openssl/providers/implementations/ciphers/cipher_cts.c',
      'openssl/providers/implementations/ciphers/cipher_tdes.c',
      'openssl/providers/implementations/ciphers/cipher_tdes_common.c',
      'openssl/providers/implementations/ciphers/cipher_tdes_hw.c',
      'openssl/providers/implementations/digests/sha2_prov.c',
      'openssl/providers/implementations/digests/sha3_prov.c',
      'openssl/providers/implementations/exchange/dh_exch.c',
      'openssl/providers/implementations/exchange/ecdh_exch.c',
      'openssl/providers/implementations/exchange/ecx_exch.c',
      'openssl/providers/implementations/exchange/kdf_exch.c',
      'openssl/providers/implementations/kdfs/hkdf.c',
      'openssl/providers/implementations/kdfs/kbkdf.c',
      'openssl/providers/implementations/kdfs/pbkdf2.c',
      'openssl/providers/implementations/kdfs/pbkdf2_fips.c',
      'openssl/providers/implementations/kdfs/sshkdf.c',
      'openssl/providers/implementations/kdfs/sskdf.c',
      'openssl/providers/implementations/kdfs/tls1_prf.c',
      'openssl/providers/implementations/kdfs/x942kdf.c',
      'openssl/providers/implementations/kem/rsa_kem.c',
      'openssl/providers/implementations/keymgmt/dh_kmgmt.c',
      'openssl/providers/implementations/keymgmt/dsa_kmgmt.c',
      'openssl/providers/implementations/keymgmt/ec_kmgmt.c',
      'openssl/providers/implementations/keymgmt/ecx_kmgmt.c',
      'openssl/providers/implementations/keymgmt/kdf_legacy_kmgmt.c',
      'openssl/providers/implementations/keymgmt/mac_legacy_kmgmt.c',
      'openssl/providers/implementations/keymgmt/rsa_kmgmt.c',
      'openssl/providers/implementations/macs/cmac_prov.c',
      'openssl/providers/implementations/macs/gmac_prov.c',
      'openssl/providers/implementations/macs/hmac_prov.c',
      'openssl/providers/implementations/macs/kmac_prov.c',
      'openssl/providers/implementations/rands/crngt.c',
      'openssl/providers/implementations/rands/drbg.c',
      'openssl/providers/implementations/rands/drbg_ctr.c',
      'openssl/providers/implementations/rands/drbg_hash.c',
      'openssl/providers/implementations/rands/drbg_hmac.c',
      'openssl/providers/implementations/rands/test_rng.c',
      'openssl/providers/implementations/signature/dsa_sig.c',
      'openssl/providers/implementations/signature/ecdsa_sig.c',
      'openssl/providers/implementations/signature/eddsa_sig.c',
      'openssl/providers/implementations/signature/mac_legacy_sig.c',
      'openssl/providers/implementations/signature/rsa_sig.c',
      'openssl/ssl/s3_cbc.c',
      'openssl/providers/common/der/der_dsa_key.c',
      'openssl/providers/common/der/der_dsa_sig.c',
      'openssl/providers/common/der/der_ec_key.c',
      'openssl/providers/common/der/der_ec_sig.c',
      'openssl/providers/common/der/der_ecx_key.c',
      'openssl/providers/common/der/der_rsa_key.c',
      'openssl/providers/common/provider_ctx.c',
      'openssl/providers/common/provider_err.c',
      'openssl/providers/implementations/ciphers/ciphercommon.c',
      'openssl/providers/implementations/ciphers/ciphercommon_block.c',
      'openssl/providers/implementations/ciphers/ciphercommon_ccm.c',
      'openssl/providers/implementations/ciphers/ciphercommon_ccm_hw.c',
      'openssl/providers/implementations/ciphers/ciphercommon_gcm.c',
      'openssl/providers/implementations/ciphers/ciphercommon_gcm_hw.c',
      'openssl/providers/implementations/ciphers/ciphercommon_hw.c',
      'openssl/providers/implementations/digests/digestcommon.c',
      'openssl/ssl/record/tls_pad.c',
      'openssl/providers/fips/fips_entry.c',

    ],
    'openssl_sources_VC-WIN64A': [
      './config/archs/VC-WIN64A/asm_avx2/crypto/aes/aes-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/aes/aesni-mb-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/aes/aesni-sha1-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/aes/aesni-sha256-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/aes/aesni-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/aes/bsaes-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/aes/vpaes-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/bn/rsaz-avx2.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/bn/rsaz-avx512.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/bn/rsaz-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/bn/x86_64-gf2m.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/bn/x86_64-mont.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/bn/x86_64-mont5.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/camellia/cmll-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/chacha/chacha-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/ec/ecp_nistz256-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/ec/x25519-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/x86_64cpuid.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/md5/md5-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/modes/aesni-gcm-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/modes/ghash-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/poly1305/poly1305-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/rc4/rc4-md5-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/rc4/rc4-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/sha/keccak1600-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/sha/sha1-mb-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/sha/sha1-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/sha/sha256-mb-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/sha/sha256-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/sha/sha512-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/crypto/whrlpool/wp-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/engines/e_padlock-x86_64.asm',
      './config/archs/VC-WIN64A/asm_avx2/providers/common/der/der_sm2_gen.c',
      './config/archs/VC-WIN64A/asm_avx2/providers/common/der/der_digests_gen.c',
      './config/archs/VC-WIN64A/asm_avx2/providers/common/der/der_dsa_gen.c',
      './config/archs/VC-WIN64A/asm_avx2/providers/common/der/der_ec_gen.c',
      './config/archs/VC-WIN64A/asm_avx2/providers/common/der/der_ecx_gen.c',
      './config/archs/VC-WIN64A/asm_avx2/providers/common/der/der_rsa_gen.c',
      './config/archs/VC-WIN64A/asm_avx2/providers/common/der/der_wrap_gen.c',

    ],
    'openssl_defines_VC-WIN64A': [
      'NDEBUG',
      'OPENSSL_BUILDING_OPENSSL',
      'OPENSSL_SYS_WIN32',
      'WIN32_LEAN_AND_MEAN',
      'UNICODE',
      '_UNICODE',
      '_CRT_SECURE_NO_DEPRECATE',
      '_WINSOCK_DEPRECATED_NO_WARNINGS',
      'AES_ASM',
      'BSAES_ASM',
      'ECP_NISTZ256_ASM',
      'FIPS_MODULE',
      'GHASH_ASM',
      'KECCAK1600_ASM',
      'OPENSSL_BN_ASM_GF2m',
      'OPENSSL_BN_ASM_MONT',
      'OPENSSL_BN_ASM_MONT5',
      'OPENSSL_CPUID_OBJ',
      'OPENSSL_IA32_SSE2',
      'SHA1_ASM',
      'SHA256_ASM',
      'SHA512_ASM',
      'VPAES_ASM',
      'X25519_ASM',
      'FIPS_MODULE',
    ],
    'openssl_cflags_VC-WIN64A': [
      '-Wa,--noexecstack',
      '/W3 /wd4090 /nologo /O2',
      '/Gs0 /GF /Gy',
      '/W3 /wd4090 /nologo /O2',
    ],
    'openssl_ex_libs_VC-WIN64A': [
      'ws2_32.lib gdi32.lib advapi32.lib crypt32.lib user32.lib',
    ],
    'linker_script': ''
  },
  'include_dirs': [
    '.',
    './include',
    './crypto',
    './crypto/include/internal',
    './providers/common/include',
  ],
  'defines': ['<@(openssl_defines_VC-WIN64A)'],

  'sources': ['<@(openssl_sources)', '<@(openssl_sources_VC-WIN64A)'],
  'direct_dependent_settings': {
    'include_dirs': ['./include', '.'],
    'defines': ['<@(openssl_defines_VC-WIN64A)'],
  },
}
