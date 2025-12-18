---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ConfigCI.Commands.dll-Help.xml
Module Name: ConfigCI
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/configci/new-cipolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-CIPolicy
---

# 新CIP政策

## 摘要
创建一个代码完整性策略，并将其保存为.xml文件。

## 语法

### 驱动程序
```
New-CIPolicy [-FilePath] <String> [-DriverFiles <DriverFile[]>] -Level <RuleLevel> [-Fallback <RuleLevel[]>]
 [-Audit] [-ScanPath <String>] [-ScriptFileNames] [-AllowFileNameFallbacks]
 [-SpecificFileNameLevel <FileNameLevel>] [-UserWriteablePaths] [-UserPEs] [-NoScript] [-Deny] [-NoShadowCopy]
 [-MultiplePolicyFormat] [-OmitPaths <String[]>] [-PathToCatroot <String>] [-AppIdTaggingPolicy]
 [-AppIdTaggingKey <String[]>] [-AppIdTaggingValue <String[]>] [<CommonParameters>]
```

### 规则
```
New-CIPolicy [-FilePath] <String> -Rules <Rule[]> [-Audit] [-ScanPath <String>] [-ScriptFileNames]
 [-AllowFileNameFallbacks] [-SpecificFileNameLevel <FileNameLevel>] [-UserWriteablePaths] [-UserPEs]
 [-NoScript] [-Deny] [-NoShadowCopy] [-MultiplePolicyFormat] [-OmitPaths <String[]>] [-PathToCatroot <String>]
 [-AppIdTaggingPolicy] [-AppIdTaggingKey <String[]>] [-AppIdTaggingValue <String[]>] [<CommonParameters>]
```

## 描述
`New-CIPolicy` cmdlet 会创建一个代码完整性策略，并将其保存为 `.xml` 文件。

如果您指定了 **DriverFile** 对象，此cmdlet将根据 **Level** 参数生成规则。然后，该cmdlet会根据这些规则为指定的驱动程序文件创建相应的策略。

如果您指定了**Rule**对象，此cmdlet将根据这些对象创建一个策略。由于您指定的规则是在特定层级上创建的，请不要指定具体的层级。

如果你既不提供驱动程序文件，也不提供规则，此cmdlet会执行类似于**Get-SystemDriver** cmdlet的系统扫描。该cmdlet会根据指定的**Level**来生成相应的规则。如果你指定了**Audit**参数，那么它将扫描代码完整性审计日志（Code Integrity Audit log）。

## 示例

### 示例 1：以多种政策格式创建一个政策
```
PS C:\> New-CIPolicy -ScanPath '.\temp\' -UserPEs -OmitPaths '.\temp\ConfigCITestBinaries' -NoScript -FilePath '.\Policy.xml' -Level Publisher -MultiplePolicyFormat
Scan completed successfully

The second command displays the contents of the policy.
PS C:\> Get-Content -Path '.\policy.xml'
<?xml version="1.0" encoding="utf-8"?>
<SiPolicy xmlns="urn:schemas-microsoft-com:sipolicy" PolicyType="Base Policy">
  <VersionEx>10.0.0.0</VersionEx>
  <BasePolicyID>{BB9EC112-DD85-41AD-9778-22680D3D8A22}</BasePolicyID>
  <PolicyID>{BB9EC112-DD85-41AD-9778-22680D3D8A22}</PolicyID>
  <PlatformID>{2E07F7E4-194C-4D20-B7C9-6F44A6C5A234}</PlatformID>
  <Rules>
    <Rule>
      <Option>Enabled:Unsigned System Integrity Policy</Option>
    </Rule>
    <Rule>
      <Option>Enabled:Audit Mode</Option>
    </Rule>
    <Rule>
      <Option>Enabled:Advanced Boot Options Menu</Option>
    </Rule>
    <Rule>
      <Option>Enabled:UMCI</Option>
    </Rule>
    <Rule>
      <Option>Disabled:Script Enforcement</Option>
    </Rule>
  </Rules>
  <!--EKUS-->
  <EKUs />
  <!--File Rules-->
  <FileRules>
    <Allow ID="ID_ALLOW_A_2F" FriendlyName="\\?\E:\cmdlets\temp\Microsoft.ConfigCI.Commands.dll Hash Sha1" Hash="BE0777
F5AF88628D4555A875036648DF1AD19BBE" />
    <Allow ID="ID_ALLOW_A_30" FriendlyName="\\?\E:\cmdlets\temp\Microsoft.ConfigCI.Commands.dll Hash Sha256" Hash="6FA5
AF724499C338A77FEEAD90F55DDF5F23D081C6DCE8E9DF486E95C6A9B310" />
    <Allow ID="ID_ALLOW_A_31" FriendlyName="\\?\E:\cmdlets\temp\Microsoft.ConfigCI.Commands.dll Hash Page Sha1" Hash="D
41570F2E6E7E6245CF342131D4706C944562B1E" />
    <Allow ID="ID_ALLOW_A_32" FriendlyName="\\?\E:\cmdlets\temp\Microsoft.ConfigCI.Commands.dll Hash Page Sha256" Hash=
"F714D9784E15B88F56180C8EE2B40C769CC83428954585A1DCF9A260FE967CDD" />
    <Allow ID="ID_ALLOW_A_37" FriendlyName="\\?\E:\cmdlets\temp\PackageInspectorTestBinaries\ntoskrnl.exe Hash Sha1" Ha
sh="FD58E1BFA1E661C809F8A2437932B0F0308A99F8" />
    <Allow ID="ID_ALLOW_A_38" FriendlyName="\\?\E:\cmdlets\temp\PackageInspectorTestBinaries\ntoskrnl.exe Hash Sha256"
Hash="A1C9FA473C2D79D0F68DF6EC72E31847F0FDA283D3A9E6B1405B0DF5929CCCB8" />
    <Allow ID="ID_ALLOW_A_39" FriendlyName="\\?\E:\cmdlets\temp\PackageInspectorTestBinaries\ntoskrnl.exe Hash Page Sha
1" Hash="6D3764B75C6502634234911B8F224FC9568217C9" />
    <Allow ID="ID_ALLOW_A_3A" FriendlyName="\\?\E:\cmdlets\temp\PackageInspectorTestBinaries\ntoskrnl.exe Hash Page Sha
256" Hash="2196AD3A00A59F4C35EEF7FE843FA3D6F80D5EFB3C674ADC087396B77AB35768" />
    <Allow ID="ID_ALLOW_A_3F" FriendlyName="\\?\E:\cmdlets\temp\PackageInspectorTestBinaries\storahci.sys Hash Sha1" Ha
sh="28FAEFE1B18A979F9FF55744B22C6E5EA2949959" />
    <Allow ID="ID_ALLOW_A_40" FriendlyName="\\?\E:\cmdlets\temp\PackageInspectorTestBinaries\storahci.sys Hash Sha256"
Hash="DA737C142A51A73D82E6AD677474C8031486FDEF018A6FE9D178564F83AB284B" />
    <Allow ID="ID_ALLOW_A_41" FriendlyName="\\?\E:\cmdlets\temp\PackageInspectorTestBinaries\storahci.sys Hash Page Sha
1" Hash="029606A9B560F4921EC1122AA73C19C9B97F7764" />
    <Allow ID="ID_ALLOW_A_42" FriendlyName="\\?\E:\cmdlets\temp\PackageInspectorTestBinaries\storahci.sys Hash Page Sha
256" Hash="2A5D6BCBFA55DB0F0487F45F4A6986AFC2C4783820EDA48DE9E0560E51D8DB56" />
    <Allow ID="ID_ALLOW_A_33" FriendlyName="\\?\E:\cmdlets\temp\Microsoft.ConfigCI.Commands.dll Hash Sha1" Hash="BE0777F5AF88628D4555A875036648DF1AD19BBE" />
    <Allow ID="ID_ALLOW_A_34" FriendlyName="\\?\E:\cmdlets\temp\Microsoft.ConfigCI.Commands.dll Hash Sha256" Hash="6FA5
AF724499C338A77FEEAD90F55DDF5F23D081C6DCE8E9DF486E95C6A9B310" />
    <Allow ID="ID_ALLOW_A_35" FriendlyName="\\?\E:\cmdlets\temp\Microsoft.ConfigCI.Commands.dll Hash Page Sha1" Hash="D
41570F2E6E7E6245CF342131D4706C944562B1E" />
    <Allow ID="ID_ALLOW_A_36" FriendlyName="\\?\E:\cmdlets\temp\Microsoft.ConfigCI.Commands.dll Hash Page Sha256" Hash=
"F714D9784E15B88F56180C8EE2B40C769CC83428954585A1DCF9A260FE967CDD" />
    <Allow ID="ID_ALLOW_A_3B" FriendlyName="\\?\E:\cmdlets\temp\PackageInspectorTestBinaries\ntoskrnl.exe Hash Sha1" Hash="FD58E1BFA1E661C809F8A2437932B0F0308A99F8" />
    <Allow ID="ID_ALLOW_A_3C" FriendlyName="\\?\E:\cmdlets\temp\PackageInspectorTestBinaries\ntoskrnl.exe Hash Sha256"
Hash="A1C9FA473C2D79D0F68DF6EC72E31847F0FDA283D3A9E6B1405B0DF5929CCCB8" />
    <Allow ID="ID_ALLOW_A_3D" FriendlyName="\\?\E:\cmdlets\temp\PackageInspectorTestBinaries\ntoskrnl.exe Hash Page Sha
1" Hash="6D3764B75C6502634234911B8F224FC9568217C9" />
    <Allow ID="ID_ALLOW_A_3E" FriendlyName="\\?\E:\cmdlets\temp\PackageInspectorTestBinaries\ntoskrnl.exe Hash Page Sha
256" Hash="2196AD3A00A59F4C35EEF7FE843FA3D6F80D5EFB3C674ADC087396B77AB35768" />
    <Allow ID="ID_ALLOW_A_43" FriendlyName="\\?\E:\cmdlets\temp\PackageInspectorTestBinaries\storahci.sys Hash Sha1" Ha
sh="28FAEFE1B18A979F9FF55744B22C6E5EA2949959" />
    <Allow ID="ID_ALLOW_A_44" FriendlyName="\\?\E:\cmdlets\temp\PackageInspectorTestBinaries\storahci.sys Hash Sha256"
Hash="DA737C142A51A73D82E6AD677474C8031486FDEF018A6FE9D178564F83AB284B" />
    <Allow ID="ID_ALLOW_A_45" FriendlyName="\\?\E:\cmdlets\temp\PackageInspectorTestBinaries\storahci.sys Hash Page Sha
1" Hash="029606A9B560F4921EC1122AA73C19C9B97F7764" />
    <Allow ID="ID_ALLOW_A_46" FriendlyName="\\?\E:\cmdlets\temp\PackageInspectorTestBinaries\storahci.sys Hash Page Sha
256" Hash="2A5D6BCBFA55DB0F0487F45F4A6986AFC2C4783820EDA48DE9E0560E51D8DB56" />
  </FileRules>
  <!--Signers-->
  <Signers>
    <Signer ID="ID_SIGNER_S_D" Name="MSIT Test CodeSign CA 3">
      <CertRoot Type="TBS" Value="FA6B9A2230CE08BCA81D096B28CF495672401D3A43A0D285CF352464A6C9C7FD" />
      <CertPublisher Value="Microsoft Windows" />
    </Signer>
    <Signer ID="ID_SIGNER_S_E" Name="MSIT Test CodeSign CA 3">
      <CertRoot Type="TBS" Value="FA6B9A2230CE08BCA81D096B28CF495672401D3A43A0D285CF352464A6C9C7FD" />
      <CertPublisher Value="Microsoft Windows" />
    </Signer>
    <Signer ID="ID_SIGNER_S_13" Name="VeriSign Class 3 Code Signing 2010 CA">
      <CertRoot Type="TBS" Value="4843A82ED3B1F2BFBEE9671960E1940C942F688D" />
      <CertPublisher Value="NVIDIA Corporation" />
    </Signer>
    <Signer ID="ID_SIGNER_S_14" Name="Microsoft Windows Third Party Component CA 2012">
      <CertRoot Type="TBS" Value="CEC1AFD0E310C55C1DCC601AB8E172917706AA32FB5EAF826813547FDF02DD46" />
      <CertPublisher Value="Microsoft Windows Hardware Compatibility Publisher" />
    </Signer>
    <Signer ID="ID_SIGNER_S_15" Name="VeriSign Class 3 Code Signing 2010 CA">
      <CertRoot Type="TBS" Value="4843A82ED3B1F2BFBEE9671960E1940C942F688D" />
      <CertPublisher Value="NVIDIA Corporation" />
    </Signer>
    <Signer ID="ID_SIGNER_S_16" Name="Microsoft Windows Third Party Component CA 2012">
      <CertRoot Type="TBS" Value="CEC1AFD0E310C55C1DCC601AB8E172917706AA32FB5EAF826813547FDF02DD46" />
      <CertPublisher Value="Microsoft Windows Hardware Compatibility Publisher" />
    </Signer>
  </Signers>
  <!--Driver Signing Scenarios-->
  <SigningScenarios>
    <SigningScenario Value="131" ID="ID_SIGNINGSCENARIO_DRIVERS_1" FriendlyName="Auto generated policy on 11-13-2015">
      <ProductSigners>
        <FileRulesRef>
          <FileRuleRef RuleID="ID_ALLOW_A_2F" />
          <FileRuleRef RuleID="ID_ALLOW_A_30" />
          <FileRuleRef RuleID="ID_ALLOW_A_31" />
          <FileRuleRef RuleID="ID_ALLOW_A_32" />
          <FileRuleRef RuleID="ID_ALLOW_A_37" />
          <FileRuleRef RuleID="ID_ALLOW_A_38" />
          <FileRuleRef RuleID="ID_ALLOW_A_39" />
          <FileRuleRef RuleID="ID_ALLOW_A_3A" />
          <FileRuleRef RuleID="ID_ALLOW_A_3F" />
          <FileRuleRef RuleID="ID_ALLOW_A_40" />
          <FileRuleRef RuleID="ID_ALLOW_A_41" />
          <FileRuleRef RuleID="ID_ALLOW_A_42" />
        </FileRulesRef>
        <AllowedSigners>
          <AllowedSigner SignerId="ID_SIGNER_S_D" />
          <AllowedSigner SignerId="ID_SIGNER_S_13" />
          <AllowedSigner SignerId="ID_SIGNER_S_14" />
        </AllowedSigners>
      </ProductSigners>
    </SigningScenario>
    <SigningScenario Value="12" ID="ID_SIGNINGSCENARIO_WINDOWS" FriendlyName="Auto generated policy on 11-13-2015">
      <ProductSigners>
        <FileRulesRef>
          <FileRuleRef RuleID="ID_ALLOW_A_33" />
          <FileRuleRef RuleID="ID_ALLOW_A_34" />
          <FileRuleRef RuleID="ID_ALLOW_A_35" />
          <FileRuleRef RuleID="ID_ALLOW_A_36" />
          <FileRuleRef RuleID="ID_ALLOW_A_3B" />
          <FileRuleRef RuleID="ID_ALLOW_A_3C" />
          <FileRuleRef RuleID="ID_ALLOW_A_3D" />
          <FileRuleRef RuleID="ID_ALLOW_A_3E" />
          <FileRuleRef RuleID="ID_ALLOW_A_43" />
          <FileRuleRef RuleID="ID_ALLOW_A_44" />
          <FileRuleRef RuleID="ID_ALLOW_A_45" />
          <FileRuleRef RuleID="ID_ALLOW_A_46" />
        </FileRulesRef>
        <AllowedSigners>
          <AllowedSigner SignerId="ID_SIGNER_S_E" />
          <AllowedSigner SignerId="ID_SIGNER_S_15" />
          <AllowedSigner SignerId="ID_SIGNER_S_16" />
        </AllowedSigners>
      </ProductSigners>
    </SigningScenario>
  </SigningScenarios>
  <UpdatePolicySigners />
  <CiSigners>
    <CiSigner SignerId="ID_SIGNER_S_E" />
    <CiSigner SignerId="ID_SIGNER_S_15" />
    <CiSigner SignerId="ID_SIGNER_S_16" />
  </CiSigners>
  <HvciOptions>0</HvciOptions>
</SiPolicy>
```

第一个命令会扫描用户模式的可执行文件（应用程序）以及内核模式的二进制文件（如驱动程序），并在“发布者”级别创建相应的规则。该命令会生成多种格式的策略，并将其存储在名为 Policy.xml 的文件中。该命令指定了 **OmitPaths** 参数，用于排除 temp\ConfigCITestBinaries 文件夹中的文件；同时，它还指定了 **NoScript** 参数，以确保仅获取可移植执行文件（PE 文件）的相关信息。

### 示例 2：扫描未签名的文件
```
PS C:\> New-CIPolicy -ScanPath '.\temp\' -UserPEs -FilePath ".\policy.xml" -Level Publisher -Fallback Hash
Unable to generate rules for all scanned files at the requested level.  A list
of files not covered by the current policy can be found at
C:\Users\tocal\AppData\Local\Temp\tmp2F2D.tmp.  If it is safe to not include
these files, no action needs to be taken, otherwise a more complete policy may
be created using the -fallback switch
```

该命令会扫描用户模式的可执行文件（应用程序）以及内核模式的二进制文件（如驱动程序），然后在发布者（Publisher）级别创建相应的规则，就像第一个示例中所做的那样。此命令没有指定 **OmitPaths** 和 **NoScript** 参数。在执行过程中，如果遇到签名格式无效或损坏的文件，该命令会返回相应的提示信息。此外，该cmdlet还会提供关于生成的规则的信息。

### 示例 3：为驱动程序文件创建规则，并将这些规则存储在一个变量中
```
PS C:\> $DriverFiles = Get-SystemDriver -ScanPath '.\temp\' -UserPEs -OmitPaths '.\temp\ConfigCITestBinaries' -NoScript
PS C:\> New-CIPolicy -Level Publisher -Fallback Hash -FilePath '.\policy02.xml' -DriverFiles $DriverFiles
```

第一个命令使用 **Get-SystemDriver** cmdlet 获取驱动程序，并将它们存储在 `$DriverFiles` 变量中。

第二个命令在发布者（Publisher）层面为存储在 $DriverFiles 中的文件创建了相应的规则。这个示例产生的效果与第二个示例中的单个命令相同。

### 示例 4：创建包含异常规则的策略
```
PS C:\> $Rule_1 = New-CIPolicyRule -Level PcaCertificate -DriverFilePath '.\temp\signedFile.exe'
PS C:\> $Exception_1 = New-CIPolicyRule -Level FileName -SpecificFileNameLevel  OriginalFileName -DriverFilePath '.\temp\FileToBlock.exe' -Deny
PS C:\> $Exception_1


Name           : C:\temp\FileToBlock.exe FileRule
Id             : ID_DENY_D_1
TypeId         : Deny
Root           :
FileVersionRef :
AppIDRef       :
Wellknown      : False
Ekus           :
Exceptions     :
FileAttributes :
FileException  : False
UserMode       : False
attributes     : {[AppIDs, ], [MinimumFileVersion, ], [FileName, FileToBlock.exe]}

Name           : C:\temp\FileToBlock.exe FileRule
Id             : ID_DENY_D_2
TypeId         : Deny
Root           :
FileVersionRef :
AppIDRef       :
Wellknown      : False
Ekus           :
Exceptions     :
FileAttributes :
FileException  : False
UserMode       : True
attributes     : {[AppIDs, ], [MinimumFileVersion, ], [FileName, FileToBlock.exe]}

PS C:\> $Exception_1[0].FileException = 1
PS C:\> $Exception_1[1].FileException = 1

PS C:\> $Rule_1[0].Exceptions += $Exception_1.ID

PS C:\> $Rule_1


Name           : Microsoft Testing PCA 2010
Id             : ID_SIGNER_S_1
TypeId         : Allow
Root           : CCEA4720A5D9D56ACFAA31C19D9D34FA4CC0771720A99DC8A2C7A4CF38A9DEE8
FileVersionRef :
AppIDRef       :
Wellknown      : False
Ekus           :
Exceptions     : {ID_DENY_D_1, ID_DENY_D_2}
FileAttributes :
FileException  : False
UserMode       : True
attributes     : {}

$Rules += $Rule_1 + $Exception_1
New-CIPolicy -MultiplePolicyFormat -FilePath ".\temp\Policy.xml" -Rules $Rules
```

第一组命令会根据用于签署测试应用程序的CA证书创建一条允许文件通过的规则，同时还会根据应用程序的原始文件名创建一条拒绝访问的规则。这条拒绝规则包含用户模式（user mode）和内核模式（kernel mode）两部分；要使该规则生效，需要将这两部分的“文件异常处理”布尔字段（file exception boolean fields）都设置为“1”。

第二组命令将“allow”文件规则的“exceptions”字段设置为该异常规则的标识符。如果“allow”规则同时包含用户模式和内核模式组件，那么这两个组件的“exceptions”字段都必须被设置为该异常规则的标识符。

最后的命令将允许文件规则的规则内容及其拒绝规则的例外情况合并到一个规则变量中，该变量可以在创建新CIPolicy（New-CIPolicy）的步骤中使用。对于包含允许例外情况的拒绝文件规则，也可以重复同样的处理过程。

文件规则异常无法使用PCA证书、发布者、签名版本或文件发布者等规则级别。

## 参数

### -AllowFileNameFallbacks
表示对于那些没有 `OriginalFileName` 的文件，系统会按照以下顺序进行处理：

- InternalName
- FileDescription
- ProductName

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AppIdTaggingKey
This parameter is reserved for future use.

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AppIdTaggingPolicy
This parameter is reserved for future use.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AppIdTaggingValue
This parameter is reserved for future use.

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Audit
Indicates that this cmdlet searches the Code Integrity Audit log for drivers.
It does not perform a full system scan.
Specify this parameter only if you do not provide driver files or rules.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: a

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Deny
Indicates that this cmdlet creates deny rules instead of the default allow rules.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: d

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DriverFiles
Specifies an array of **DriverFile** objects on which this cmdlet bases rules.
To obtain a driver file, use the **Get-SystemDriver** cmdlet.

```yaml
Type: DriverFile[]
Parameter Sets: Drivers
Aliases: df

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Fallback
Specifies an array of levels of detail for generated rules.
If this cmdlet cannot generate a rule at the specified level, this cmdlet attempts to generate it at a fallback level.
The acceptable values for this parameter are the same as for **Level**.
If you specify multiple fallback levels, this cmdlet tries them in order.

```yaml
Type: RuleLevel[]
Parameter Sets: Drivers
Aliases:
Accepted values: None, Hash, FileName, FilePath, SignedVersion, PFN, Publisher, FilePublisher, LeafCertificate, PcaCertificate, RootCertificate, WHQL, WHQLPublisher, WHQLFilePublisher

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FilePath
Specifies the path for the Code Integrity policy .xml file.

```yaml
Type: String
Parameter Sets: (All)
Aliases: f

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Level
Specifies the primary level of detail for generated rules. Refer to [WDAC File Rule Levels](/windows/security/threat-protection/windows-defender-application-control/select-types-of-rules-to-create#windows-defender-application-control-file-rule-levels) for acceptable parameter values and descriptions.

```yaml
Type: RuleLevel
Parameter Sets: Drivers
Aliases: l
Accepted values: None, Hash, FileName, FilePath, SignedVersion, PFN, Publisher, FilePublisher, LeafCertificate, PcaCertificate, RootCertificate, WHQL, WHQLPublisher, WHQLFilePublisher

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MultiplePolicyFormat
Indicates that this cmdlet should create a policy in multiple policy format as opposed to a single policy format.
Refer to [Create WDAC policies in Multiple Policy Format](/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies#creating-wdac-policies-in-multiple-policy-format) for the difference between the policy formats.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoScript
Indicates that this cmdlet does not search script files.
It searches portable executable files (PE files) only.
Specify this parameter only if you do not provide driver files or rules.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoShadowCopy
Indicates that the Volume Snapshot Service (VSS) does not make a shadow copy of the disk while the scan runs.
This parameter could cause an incomplete scan for a system that is running.

If a scan fails due to VSS errors caused by low disk space on the target drive, this cmdlet prompts you to specify this parameter.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OmitPaths
Specifies an array of paths that this cmdlet omits from the search.
Specify this parameter only if you do not provide driver files or rules.
We recommend that you omit C:\Windows.old.

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: o

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PathToCatroot
Specifies the path of the CatRoot folder.
Specify this parameter to scan a remote or mounted drive.
Specify this parameter only if you do not provide driver files or rules.

```yaml
Type: String
Parameter Sets: (All)
Aliases: c

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Rules
Specifies an array of **Rule** objects that this cmdlet includes in the policy.
To obtain a rule object, use the **Get-CIPolicy** or **New-CIPolicyRule** cmdlets.

```yaml
Type: Rule[]
Parameter Sets: Rules
Aliases: r

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ScanPath
Specifies the path for this cmdlet to scan.
You can specify a local or remote path.
Specify this parameter only if you do not provide driver files or rules.
If you specify a remote or mounted drive, also specify the **PathToCatroot** parameter.

```yaml
Type: String
Parameter Sets: (All)
Aliases: s

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScriptFileNames
This parameter is reserved for internal Microsoft use.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SpecificFileNameLevel
Specifies the attribute of the file off which to base a file name rule. The -Level must be set to FileName for this option. Possible values are: None, OriginalFileName, InternalName, FileDescription, ProductName, PackageFamilyName, and FilePath.
Refer to [File Name Rules Info](/windows/security/threat-protection/windows-defender-application-control/select-types-of-rules-to-create#windows-defender-application-control-filename-rules) for a description of the acceptable values.

```yaml
Type: FileNameLevel
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UserPEs
Indicates that this cmdlet includes user-mode files in the scan.
Specify this parameter only if you do not provide driver files or rules.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: u

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UserWriteablePaths
Indicates that this cmdlet includes files identified as user writeable in the policy.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-CIPolicy](./Get-CIPolicy.md)

[Get-SystemDriver](./Get-SystemDriver.md)

[Merge-CIPolicy](./Merge-CIPolicy.md)

[New-CIPolicyRule](./New-CIPolicyRule.md)
