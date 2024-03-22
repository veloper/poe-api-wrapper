import json, random

QUERIES = {
  "RegenerateMessageMutation": "056f5f4b6a39ca7786a4f0b2ef37eee401c81d6086cd78ffc12fe2ce0bccb1fd",
  "AddEmailMutation": "6d9ff3c8ed7badced30cfdad97492d4c21719931e8c44c5601abfa429b62ded7",
  "ChatHelpers_addMessageBreakEdgeMutation_Mutation": "9450e06185f46531eca3e650c26fa8524f876924d1a8e9a3fb322305044bdac3",
  "SendChatBreakMutation": "79ad99fa0c899c2d5b6d1a10b1f46b77cbd5f99dd77bac4dbd6cc0cb0b79a779",
  "AddPhoneNumber": "26ae865f0686a910a86759c069eb1c0085d78b55a8abf64444ec63b03c76fb58",
  "AnnotateWithIdsProviderQuery": "b4e6992c3af8f208ab2b3979dce48889835736ed29f623ea9f609265018d0d8f",
  "AvailableBotsListModalPaginationQuery": "3be373baa573ccd196b9d71c94953b1d1bc586625bd64efe51655d75e68bbfb7",
  "AvailableBotsSelectorModalPaginationQuery": "26214d2e2381b435992200b171b9f39f360cfd5d668c71b071d5575aa6c3c10e",
  "BotInfoFormRunCheckMutation": "87d55551061151b852fd7c53ec34dbb1ae784516b0ba2df5255b201f0d4e1444",
  "BotInfoModalQuery": "33254e9e91d63d16dbac1d70aa6accfb31786be05f7749772a32bc37d9ccb799",
  "BotLandingPageQuery": "18c8cd1a9e0707e93cf44d31e909809b05ceedcd2d10cdf7d1c49a82f6718e09",
  "BotSelectorModalQuery": "6e9a70b8e98922d018d12e87474124b766287137dcbdf06eda74d2e14c357aa7",
  "BotSwitcherModalQuery": "54023ee8b691543982b2819491532532c317b899918e049617928137c26d47f5",
  "ChatDeleteConfirmationModalQuery": "716c8cc3ac6c13d6b41ceb2404e3a28c63aea6d166bf071dca1f98e0377727c3",
  "ChatHelpersSendNewChatMessageMutation": "de5e755e5887f89b558abb7dbbe67cd459dd89f088957e4146253c29942576b0",
  "ChatHistoryFilteredListPaginationQuery": "b27c110fc75c59a23b660438b209a699f3911a7d3902e2a8e9728d2cc1c5d5b9",
  "ChatHistoryListPaginationQuery": "6ce01455b0201e625489da90c65f87a2809d212ea41ab6e39412b6913990e81f",
  "ChatHomeMainInputContainerOptimisticBotQuery": "1c9267ecff73cb27a8e7d94a3f5b5fe665a82abe0fdd61be2e54dd38c0e61639",
  "ChatHomeMainInputContainerOptimisticViewerQuery": "21f0eb43ab07d97d4a30bcf007db4797b95e852fb6537e8dbbc002da45ba4fac",
  "ChatListPaginationQuery": "e109d61fff512d58d84989aae2418a19167e3b6a9626d795b8a4f2bc84daf97c",
  "ChatLoaderQuery": "d9467ac216e21b510eb8e72a2888289d173c9d5ce399b072fd88bee3da1b1459",
  "ChatPageBotBotsPagination": "ed9017f85fe2fedbf02b2d000cb4b551d2ec870715d0c7bce6d54a0f3f9b657b",
  "ChatPageQuery": "bb1c03fdd36312466c5817f1b914229ac2105d99f78930778f8d8d500102e10a",
  "ChatsHistoryPageQuery": "9276a572d279d5d0e9704531d8572eb626904c414d2f40370055f2d712058a12",
  "ChatSetTitle": "24574aab7fedf86d1654bbc70bf5421abbc33e195aa1c11178697023a27a912e",
  "ChatSettingsModalQuery": "41910ff112abaa713edd836cbb7fc567433f3f7ac3a61659fffca6306f7288ac",
  "ChatSubscriptionPaywallModalQuery": "559ac4c7c8f0f6f50148d255bb6318107034375df7bca4214f608cd65b573a21",
  "ChatSwitcherRefetchQuery": "815b8e6406bd19b25da36523b8b33c8c25e6db2fe93505117bb583c2d9dd60e4",
  "ChatTitleUpdated": "ee062b1f269ecd02ea4c2a3f1e4b2f222f7574c43634a2da4ebeb616d8647e06",
  "ContinueChatFromPoeShare": "a220810c2d1d3b5284b6be44309a3d2b197c312a79b1a27f165a12f1508322bd",
  "ContinueChatIndexPageQuery": "a7eea6eebd14aa355723514558762315d0b4df46205b70f825d288d5ed1635ec",
  "ContinueChatPageQuery": "fe3a4d2006b1c4bb47ac6dea0639bc9128ad983cf37cbc0006c33efab372a19d",
  "CreateBotIndexPageQuery": "0d7db3055a91d8574628b81f4e5ed23309bacb90cab08ac3ab7e32d67a72fd22",
  "CreateBotPageQuery": "4fa5e0703c416fc6b40c5e2fcfcac66301ed0c8d32bafb5d69300e7553ef1f8f",
  "CreateChatMutation": "f1322c9c34d4140d420aeb9151cdeebc2235d381ada0037c845572310f613b7d",
  "CreateChatWithTitle": "6cf8cddd6594901bd4a7dc6ddeffc91485c21c817e8f7fa07fae9d71d9807d71",
  "CreateCheckoutSession": "5eb43e7c83974acc6680e1abe4c169296d0b346c42cc20d487762163402ea8e5",
  "CreateCustomerPortalSession": "4d43136f33aba6b6dea2ac8cd295e03bd841b7c99bf772940fa06a623a331786",
  "CreateMessagesToContinueChatMutation": "00b66f0117fab1ab6cdcf7e98819c1e3196736253b6a158316a49f587b964d25",
  "DeleteAccountMutation": "4e9651277464843d4d42fbfb5b4ccb1c348e3efe090d6971fa7a3c2cabc7ea5c",
  "DeleteChat": "5df4cb75c0c06e086b8949890b1871a9f8b9e431a930d5894d08ca86e9260a18",
  "DeleteMessageMutation": "8d1879c2e851ba163badb6065561183600fc1b9de99fc8b48b654eb65af92bed",
  "DeleteUserMessagesMutation": "3f60d527c3f636f308b3a26fc3a0012be34ea1a201e47a774b4513d8a1ba8912",
  "DismissDismissible": "b133084411c0a7a2353f6cfacd3d115260c34ddc5d97cf7f19a16e8cb4410803",
  "EditBotIndexPageQuery": "4b19c8068312a192bd37aee05adcfbb91e65379a85a6cae3b7f3ffdd0eeed9b1",
  "EditBotPageQuery": "67c96902edcb66854106892671c816d9f7c3d8910f5a6b364f8b9f3c2bc7a37a",
  "EmailUnsubscribe": "eacf2ae89b7a30460619ccfb0d5a4e6007cfbcf0286ec7684c24192527a00263",
  "EmbedLoggedOutPageQuery": "e81580f4126215186e8a5d18bdedcf7c056b634d4d864f54b948765c8c21aef9",
  "ExploreBotsCarouselContainerQuery": "e46511b51cb2e9244225e1e6509c6a696dde271e45da74ce66853379eaeb80d6",
  "ExploreBotsCarouselLazyLoadedContainerQuery": "846522f24edbbad1331cedfe311ba0c8e365cf33aee1bb1e3f0e03156f1a0536",
  "ExploreBotsCarouselPagedContainerPaginationQuery": "619df00e336f6bbad2bbc2626aa74f97eb12efb50f403339cc780041aa9897e0",
  "ExploreBotsIndexPageQuery": "96026f5201635559989830b63ec55dcf6080abe8152a52f39ffb98b46d6850d4",
  "ExploreBotsListPaginationQuery": "91c2b3d288db2bd7018f954414a12123f745c243709b02a9216d575d2c0fe8c9",
  "ExploreBotsPageQuery": "be8c7ca9725a477d6b04f907f3c0f0f58dd7647550555811720ffbac3c90ecfb",
  "ExploreBotsSidebarQuery": "00f42e3842c63cfcfcebad6402cdaa1df1c3fa7ffe3efbe0437a08a151eca87e",
  "GenerateAppleAuthNonceMutation": "c3e0c1b990cd17322716d0fa943a8ddc0ffecf45294ad013ccc883954c2171fc",
  "HandleBotChatEmbedPageQuery": "60a48e1b772e6830ddbdb54f19e837beef949d4fc146c51b1f50469f40b7650b",
  "HandleBotChatPageQuery": "dc1891a1d9b3ca42c773a69e9985f95e78a13ad5858cef0574c7f4ce87004a77",
  "HandleBotLandingPageQuery": "32da0efe74b35629c46ed61470b6e2f38f67fd9e95b9c44a7dea0f39a445bafe",
  "HandleProfileIndexPageQuery": "0243e1784c33ae913d8a3ad20fc1252b930b6741ff9d78bd776e2df4f93f55ee",
  "HandleProfilePageQuery": "61b9722aa439c027110908b160db683f623e8affcde2d5f66378375b9ae668e3",
  "IntroMainQuery": "47f2c9bb41be5238968c81c82f2d2cff4100c73fcc70a9f592825bb40c0efc8d",
  "LayoutLeftSidebarQuery": "073fc8aad11bae987f5b70a68a0c2fedf8c8b3f2702757cdc68f8aedd1ee8103",
  "LayoutRightSidebarQuery": "357308110e99687fefcf5f4987bbfdf8427bf9b2fd512e265f6cc8a93ee0c9ae",
  "LoginPageQuery": "538d23244211dfe6ed3228518508ebc728f9f8165950d5a19fc5467c2f0b9a1f",
  "LoginWithVerificationCodeMutation": "0d5aecd57239d518c25dc972569ee77dd9610a114610a6a3e87b87fdd8f1ba90",
  "LogoutAllSessionsMutation": "1e62b26302959ca753def8678e817b2c1ad94efdb21872dbf0f8bffcb892aed4",
  "LogoutMutation": "1d2e52b19e15a6aa0ec93d8e4a3a9653b9ceb4c1f365c7d9c4451d835505eef2",
  "MarkAndroidAppDownloadPromptSeen": "ed6891c8913983cc4fd0bfed9760e9738743419712ce6681841217ed0bb8c915",
  "MarkMultiplayerNuxCompleted": "c1b1f2ce72d9f8e9cd7bbe1eecbf6e3bed3366df6a18b179b07ddfd9f1f8b3b1",
  "MessageAdded": "0b8de439cec33e6b2a248117241e2d3e166629c777462d0b3332e3a417d952ed",
  "Knowledge_CreateKnowledgeSourceMutation": "53a8daf2cb85b0d4f17520a0fbad1ee8c402d4e85a5ba3c5856563299b13ee98",
  "Knowledge_EditKnowledgeSourceMutation": "627557c27853ba0d52ceb77e58116034f103d60a5b00bf5e0c5edd2af6b21827",
  "EditBotIndexPageQuery": "4b19c8068312a192bd37aee05adcfbb91e65379a85a6cae3b7f3ffdd0eeed9b1",
  "StopMessage_messageCancel_Mutation": "d2d75098e1878758a5bcd39c89ff6c8c7f5fd633a4f432c234fede8cb743c2e6",
  "MessageCancelled": "14647e90e5960ec81fa83ae53d270462c3743199fbb6c4f26f40f4c83116d2ff",
  "MessageDeleted": "91f1ea046d2f3e21dabb3131898ec3c597cb879aa270ad780e8fdd687cde02a3",
  "MessageCreated": "26847fdf99c61144d75b62d3c6a6e959667a6d48190256bbef2e90d41ce3b931",
  "MessageCitationSourceModalQuery": "ad19832b5d80a626449366a6b1ff0f43272a4324e5d0bd586dbce67922edbd2c",
  "KnowledgeSourceUpdated": "7de63f89277bcf54f2323008850573809595dcef687f26a78561910cfd4f6c37", 
  "MessageLimitUpdated": "daec317b69fed95fd7bf1202c4eca0850e6a9740bc8412af636940227359a211",
  "MessageUnvoteMutation": "af2b91f09ab2ccf53ba9176a86b9934b98a865adf228b2ac3a548d6397f382f3",
  "MessageVoteMutation": "199fd8402c70ac10c5b05ba31587a0beff3acc39c7194362610ad50bf20299ed",
  "NewLandingPageQuery": "f36fbfcbad84b02876a254ba77ecf78f96360e77291766209b9e7655852440da",
  "NumTokensFromPromptQuery": "1d9bef79811f3b2ddca5ce4027b7eaa31a51bbeed1edf8b6f72e2e0d09d80609",
  "NuxInitialModalQuery": "f8cd0d8494afe3b5dbb349baa28d3ac21f2219ce699e2d59a2345c864905e0c3",
  "NuxInitialModal_poeSetHandle_Mutation": "93a0c939986bb344f87a76d9d709f147a23f1a45ec26e291bcea9acf66b3215f",
  "OnboardingFreeTrialModalQuery": "d2cc659e3def4561ca15b268a97588c5af6cd154afb001312aa69f63c5b2cc9e",
  "OnboardingPaywallModalQuery": "b413e41e89125528f1b2e7f472bde37f6f48a25cb774f4ea3ff883644c973cca",
  "OnboardingPaywallWithGraphicModalQuery": "f986cd3dc4fbab98927983c5d4ed78fa095af78392cf3880af9203dea975890d",
  "OptimisticChatLoaderQuery": "8633378bbe67e397457bebb256d7dc0c48f9a973315f3158cfb2f4fc08ad6c06",
  "PageBlockerQuery": "d1ab792fce4d3f91777b49856d44b2d9cbb6ad1231e1116c407a0208604181e1",
  "PageWrapperQuery": "fa2f44e7aafe6d1698f88ef7443fe13727765570ab504555a15d9c1578ded275",
  "PagesBotNameQuery": "a156136af92b189768540f864445f0b8d9191584530def6b1a5502c843539cfb",
  "PagesDefaultBotChatPageQuery": "75bd0877369c2b4191c936572822ce1875c980f1f6f8683381bd4a6850bdea92",
  "BotInfoCardActionBar_poeBotDelete_Mutation": "ddda605feb83223640499942fac70c440d6767d48d8ff1a26543f37c9bb89c68",
  "BotInfoCardActionBar_poeRemoveBotFromUserList_Mutation": "5dd4da93f99a2daf629f082b6a4938d940833e8054b5f4f611d9c8c1928b0dc4",
  "PoeBotCreate": "384184cd2e904bb0da2ce55ad2b36fd320463e52572147f6663aa53be26cc8e7",
  "PoeBotDelete": "b446d0e94980e36d9ba7a5bc3188850186069d529b4c337fb9e91b9ead876c12",
  "PoeBotEdit": "715949794448a572858f879b09730008f41cbea1c1934f4b53268d8ffc97c6e0",
  "PoeBotFollow": "efa3f25f6cd67f9dea757be50305c0caa6a4e51f52ffba7e4a1c1f2c84d6dbd0",
  "PoeBotUnfollow": "db2281f3efa305db62d38964b640e982076491c2c59d5be3303feae343fe8914",
  "PoeRemoveBotFromUserList": "89e756b668b2318fa73c2a9dde4608a4529c74844667417c0cfb245e7e04e96e",
  "PoeSetBio": "66fb99ec59fa17bc4487f944d116bc920161faced58a3ce99e82cb61af61468e",
  "PoeSetHandle": "4139b28c6a152e2d074944a7cf7f133b453080c1660c4960e14418be363897bb",
  "PoeSetName": "c406a46fe6ff244ab2d665ea953fc8655d6816f1731505d830863d9b9c5021bf",
  "PoeSetProfilePhoto": "13106f2433e5d48a53e6804b76022e80c0fc9bf018eb5b5404d9e0a4acd94f1f",
  "PoeUserSetFollow": "dcc26e4e36b47af8af6bd0296ff85dfa8fc77a9c374ea5989afd0bf39ae4d35e",
  "PostIdPostPageQuery": "653c4768688ce6c8c14ca359ce536646b3de71a7e953c16381136399791c95a0",
  "ProfileIndexPageQuery": "4044ca7eb203e613f19dc76a4a05ca1df25bfdb2ff761a9d6dced6b0d61f219a",
  "ProfilePageQuery": "9505daf59f885463e5bd3bb2a1a9fc088e8634fbc7d5a0682f2ece11ee7548dd",
  "RemoveEmailMutation": "63750a7e41cc0ad3f6da0be1fdae9c243f1afab83cf44bb5c3df14243074681d",
  "RemoveUserPhoneNumberMutation": "7dadad6ac75a8a4e5c54479524c7821e748c043242476958262bb39fa60ccddb",
  "SaveContinueChatInfoMutation": "ae56678376401ae45dbba61aa6b1a55564877edc33605db6283e1dc3bdb0c8ff",
  "SearchResultsListPaginationQuery": "f6d4b5bbec10438548a5f8feedac11001878efe2e31a3d0ecd7680a4decb5c66",
  "SearchResultsMainQuery": "7ee1c22fd46693de7869ce0305d0209b7fda41ef91389110cd989804194fcaf8",
  "SelectorTestPageQuery": "9ec86fe8e3d0d3b264d0fab0feb73e38c86d616c7c3d8340d7a6146bd8445ed3",
  "SendMessageMutation": "3e1b3b88bf74f5c4e8a15a2d92740dec450dfa2e46a6ff586beb44378c277510",
  "SendVerificationCodeMutation": "d418fa3d2357d089b20065226041180573fa0b0382914a90cf905435281af520",
  "SetPrimaryEmailMutation": "01e75a6d937351b304ca9cc0b231e43587a5923e7f8618863bdf996df38d28b5",
  "SettingsDefaultBotSectionMutation": "4084604e8741af8650ac6b4236cdfa13c91a70cf1c63ad8a368706a386d0887e",
  "SettingsIndexPageQuery": "c9cab56d7329fc2665760ceeb92005e2b3449351a5fb24d906e52587ca87ca64",
  "SettingsPageQuery": "1633485f58c7f2e730a34446b8566c40b5fe2a75ad82b930e3374d8c222b5983",
  "ShareCodeSharePageQuery": "e56f5cb9c7fc9872d053ddaef3dd7827067530b014f59e3ed07bc5e21a0f4334",
  "ShareMessageMutation": "2491190f42c1f5265d8dbaaaf7220dbfa094044fdfb2429fd7f2e35f863bc5e1",
  "ContinueChatCTAButton_continueChatFromPoeShare_Mutation": "8b7bbb788463708e87ea979a383ddf6cbbb8818305add8b30c275a13ce9c7a95",
  "SignupOrLoginWithAppleMutation": "649943f9929600796b30f48a47094af56a5d86b4556e34e91aa8ea834cda5fda",
  "SignupOrLoginWithGoogleMutation": "519c2241faeb2bade473ed190913365604eee13ca97b67775b2c7b1aad0fb095",
  "SignupOrLoginWithQuoraMutation": "ee2498e8837e7b975806613401f5aa4ba18d03fdcc9fde0c59efc75717103df5",
  "SignupWallModalInnerQuery": "56f7718c8e586c16065f7b57dcbcf61d3789ab937590e8e77d458613b3c8f325",
  "SignupWithVerificationCodeMutation": "6a9b90b76ee9c058f55a3d659c093a5eca6a5ddbef233dbecee389501b1e5dbf",
  "StaticContentQuery": "15267bf130fbe298a6f60334f57ccf62bc16ff06c74d5778ba54b4b4f21f8d0c",
  "SubscriptionTosQuery": "6696950c5612023d877acd6a6f9026668960994825d3fa71a80528c316510c2f",
  "SubscriptionsMutation": "5a7bfc9ce3b4e456cd05a537cfa27096f08417593b8d9b53f57587f3b7b63e99",
  "UniversalLinkPageQuery": "ec7c629dd6ec79f9d26dda9c4ef9cb1e24aa41d7b92090596b6639eeee5e6cc8",
  "UpdatePhoneNumber": "c49f5f64947c2946f8007f366bbc0ca5b1f0bbbdc6b72ad97be90533f0e83c28",
  "UseBotSelectorBotQuery": "6af7249e90de59baef2e770f7e773f9f7730fd49db6b4e82035c49a078818534",
  "UseBotSelectorViewerBotsPaginationQuery": "e7dbf27efba69f014750ee56ac13f21262e76e161c6e58d435ae75935798d1b0",
  "UseStopMessageAndSendChatBreak": "9b95c61cd6cb41230a51fb360896454dde1ae6d1edb6f075504cb83a52422bc9",
  "UserEditBioModalQuery": "b78089f19d1071ad9440d5a2696588b0e82a012f6b40dca68f071cc0a49727f2",
  "UserEditHandleModalQuery": "ecee1f772c401f6e429ba7ebe088eedc0aa6d24dfa4cae0ec6f54bb3c5a5c653",
  "UserEditNameModalQuery": "dd72d69698a46097386b73b19677a84b6bcba51b3df3790e67d804b6da686787",
  "UserEditProfilePicModalQuery": "7f69ff6407a1360570863b09a9c02bf0a4bdbd8de2b04e5dde4eec031a6f62e5",
  "UserFolloweesListModalQuery": "b219f7e8b7c8d21aaa0979d44bfc3935501719e3fe18cbe86b459eced5f290d2",
  "UserFollowersListModalQuery": "86b007fa15b2de6f7eb527050832d342dde837aaedfb61bfdd1bf1201b860b61",
  "UserProfileConfigurePreviewModalQuery": "abec61f90eebcc3b914487db0ba35ff6ec53c1f7c29f40f59222cee5b8832a52",
  "ViewerStateUpdated": "5ae4027023f0513bf3a402323333b8b99e931bf9df28390099613e4ab0cde018",
  "WebSpeedUpsellQuery": "d8556da659d21dc2c583248c1c617ca20492b64c6948ae4a16256c0848f9c32e",
  "WebSubscriptionAnnouncementQuery": "a1b332d7d6816accfccb619e0f0728771ac7c398881fa423051d06551cd0f069",
  "WebSubscriptionPaywallModalQuery": "4d248f3aa4fbf68eb57a1bdda52a6dc5f38dd3b1234c01a95d4b17fdfbd922db",
  "WebSubscriptionPaywallWrapperQuery": "f84fada22609f5dc5933e7ef1e54001fa5e76871836f268e68ad8df7e202f6ca",
  "MessageCitationSourceModalQuery": "ad19832b5d80a626449366a6b1ff0f43272a4324e5d0bd586dbce67922edbd2c",
}

def generate_payload(query_name, variables) -> str:
    if query_name == "recv":
        return generate_recv_payload(variables)
    payload = {
        "queryName": query_name,
        "variables": variables,
        "extensions": {
            "hash": QUERIES[query_name]
        }
    }
    return json.dumps(payload, separators=(",", ":"))

def generate_recv_payload(variables):
    payload = [
    {
      "category": "poe/bot_response_speed",
      "data": variables,
    }
    ]

    if random.random() > 0.9:
        payload.append({
        "category": "poe/statsd_event",
        "data": {
            "key": "poe.speed.web_vitals.INP",
            "value": random.randint(100, 125),
            "category": "time",
            "path": "/[handle]",
            "extra_data": {},
        },
        })
    return json.dumps(payload, separators=(",", ":"))