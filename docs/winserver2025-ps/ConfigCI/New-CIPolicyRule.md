---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ConfigCI.Commands.dll-Help.xml
Module Name: ConfigCI
ms.date: 05/23/2022
online version: https://learn.microsoft.com/powershell/module/configci/new-cipolicyrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-CIPolicyRule
---

# 新CIP政策规则

## 摘要
为用户模式代码和驱动程序生成代码完整性策略规则。

## 语法

### DriverFileList
```
New-CIPolicyRule [-DriverFiles <DriverFile[]>] -Level <RuleLevel> [-Fallback <RuleLevel[]>] [-Deny]
 [-ScriptFileNames] [-AllowFileNameFallbacks] [-SpecificFileNameLevel <FileNameLevel>] [-UserWriteablePaths]
 [<CommonParameters>]
```

### DriverFilePath
```
New-CIPolicyRule -DriverFilePath <String[]> [-AppID <String>] -Level <RuleLevel> [-Fallback <RuleLevel[]>]
 [-Deny] [-ScriptFileNames] [-AllowFileNameFallbacks] [-SpecificFileNameLevel <FileNameLevel>]
 [-UserWriteablePaths] [<CommonParameters>]
```

### PackageFamilyName
```
New-CIPolicyRule [-Fallback <RuleLevel[]>] [-Deny] [-ScriptFileNames] [-AllowFileNameFallbacks]
 [-SpecificFileNameLevel <FileNameLevel>] [-UserWriteablePaths] [-Package <AppxPackage>] [<CommonParameters>]
```

### ManualFilePath
```
New-CIPolicyRule [-Fallback <RuleLevel[]>] [-Deny] [-ScriptFileNames] [-AllowFileNameFallbacks]
 [-SpecificFileNameLevel <FileNameLevel>] [-UserWriteablePaths] [-FilePathRule <String>] [<CommonParameters>]
```

## 描述
`New-CIPolicyRule` cmdlet 用于为驱动程序生成代码完整性（Code Integrity）策略规则。你需要指定规则的级别，以及一个 `DriverFile` 对象数组或驱动程序的路径。

## 示例

### 示例 1：为驾驶员创建策略规则
```
PS C:\> $DriverFiles = Get-SystemDriver -ScanPath '.\temp\' -UserPEs -OmitPaths '.\temp\ConfigCITestBinaries' -NoScript
PS C:\> New-CIPolicyRule -Level FileName -DriverFiles $DriverFiles
Scan completed successfully


Name           : \\?\E:\cmdlets\temp\Microsoft.ConfigCI.Commands.dll FileRule
Id             : ID_ALLOW_A_1
TypeId         : Allow
Root           :
FileVersionRef :
Wellknown      : False
Ekus           :
Exceptions     :
FileAttributes :
FileException  : False
UserMode       : False

Name           : \\?\E:\cmdlets\temp\Microsoft.ConfigCI.Commands.Tests.dll FileRule
Id             : ID_ALLOW_A_3
TypeId         : Allow
Root           :
FileVersionRef :
Wellknown      : False
Ekus           :
Exceptions     :
FileAttributes :
FileException  : False
UserMode       : False

Name           : \\?\E:\cmdlets\temp\Microsoft.PackageInspector.Tests.dll FileRule
Id             : ID_ALLOW_A_5
TypeId         : Allow
Root           :
FileVersionRef :
Wellknown      : False
Ekus           :
Exceptions     :
FileAttributes :
FileException  : False
UserMode       : False
```

第一个命令使用 **Get-SystemDriver** cmdlet 获取驱动程序，并将它们存储在 `$DriverFiles` 变量中。

第二个命令为 `$DriverList` 中列出的驱动程序在文件名级别创建策略规则。在这个示例中，我们仅展示前几条规则。

### 示例 2：为驾驶员创建策略规则，并包含一个备用值
```
PS C:\> New-CIPolicyRule -Level Publisher -Fallback Hash -DriverFiles $DriverFiles
"Scan completed successfully"


Name           : \\?\E:\cmdlets\temp\Microsoft.ConfigCI.Commands.dll Hash Sha1
Id             : ID_ALLOW_A_F
TypeId         : Allow
Root           :
FileVersionRef :
Wellknown      : False
Ekus           :
Exceptions     :
FileAttributes :
FileException  : False
UserMode       : False

Name           : \\?\E:\cmdlets\temp\Microsoft.ConfigCI.Commands.dll Hash Sha256
Id             : ID_ALLOW_A_10
TypeId         : Allow
Root           :
FileVersionRef :
Wellknown      : False
Ekus           :
Exceptions     :
FileAttributes :
FileException  : False
UserMode       : False

Name           : \\?\E:\cmdlets\temp\Microsoft.ConfigCI.Commands.dll Hash Page Sha1
Id             : ID_ALLOW_A_11
TypeId         : Allow
Root           :
FileVersionRef :
Wellknown      : False
Ekus           :
Exceptions     :
FileAttributes :
FileException  : False
UserMode       : False
```

此命令为上一个示例中提到的相同驱动程序在发布者（Publisher）级别生成相应的规则。对于未签名的文件，该cmdlet会创建哈希规则作为备用方案。在这个示例中，我们仅展示前几条规则。

### 示例 3：为内核组件指定一条策略规则
```
PS C:\> New-CIPolicyRule -DriverFilePath '.\temp\ConfigCITestBinaries\ci.dll' -Level Publisher
Scan completed successfully


Name           : MSIT Test CodeSign CA 3
Id             : ID_SIGNER_S_B
TypeId         : Allow
Root           : FA6B9A2230CE08BCA81D096B28CF495672401D3A43A0D285CF352464A6C9C7FD
FileVersionRef :
Wellknown      : False
Ekus           :
Exceptions     :
FileAttributes :
FileException  : False
UserMode       : False

Name           : MSIT Test CodeSign CA 3
Id             : ID_SIGNER_S_C
TypeId         : Allow
Root           : FA6B9A2230CE08BCA81D096B28CF495672401D3A43A0D285CF352464A6C9C7FD
FileVersionRef :
Wellknown      : False
Ekus           :
Exceptions     :
FileAttributes :
FileException  : False
UserMode       : True
```

该命令为名为 ci.dll 的特定文件生成一条发布者规则。ci.dll 文件是一个内核组件，因此这个 cmdlet 会同时生成一条针对内核模式的规则和一条针对用户模式（user mode）的规则。

### 示例 4：为包含通配符的文件夹路径指定策略规则
```
PS C:\> New-CIPolicyRule -FilePathRule '.\temp\ConfigCITestBinaries\*'


Name           : .\temp\ConfigCITestBinaries\* FileRule
Id             : ID_ALLOW_A_1
TypeId         : Allow
Root           :
FileVersionRef :
AppIDRef       :
Wellknown      : False
Ekus           :
Exceptions     :
FileAttributes :
FileException  : False
UserMode       : True
attributes     : {[AppIDs, ], [MinimumFileVersion, 0.0.0.0], [FilePath, .\temp\ConfigCITestBinaries\*]}
```

这个命令会为指定的路径生成一个文件路径规则（即字符串形式的文件路径）。这样，父文件夹中的任何内容都可以被访问或操作。

### 示例 5：为打包的应用程序及其依赖项创建策略规则
```
PS C:\> $packages = Get-AppxPackage -Name *Microsoft*
PS C:\> $packages

Name              : Microsoft.NET.Native.Runtime.1.4
Publisher         : CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US
Architecture      : X86
ResourceId        :
Version           : 1.4.24201.0
PackageFullName   : Microsoft.NET.Native.Runtime.1.4_1.4.24201.0_x86__8wekyb3d8bbwe
InstallLocation   : C:\Program Files\WindowsApps\Microsoft.NET.Native.Runtime.1.4_1.4.24201.0_x86__8wekyb3d8bbwe
IsFramework       : True
PackageFamilyName : Microsoft.NET.Native.Runtime.1.4_8wekyb3d8bbwe
PublisherId       : 8wekyb3d8bbwe
IsResourcePackage : False
IsBundle          : False
IsDevelopmentMode : False
NonRemovable      : False
IsPartiallyStaged : False
SignatureKind     : Store
Status            : Ok
...
Name              : Microsoft.NET.Native.Runtime.1.4
Publisher         : CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US
Architecture      : X64
ResourceId        :
Version           : 1.4.24201.0
PackageFullName   : Microsoft.NET.Native.Runtime.1.4_1.4.24201.0_x64__8wekyb3d8bbwe
InstallLocation   : C:\Program Files\WindowsApps\Microsoft.NET.Native.Runtime.1.4_1.4.24201.0_x64__8wekyb3d8bbwe
IsFramework       : True
PackageFamilyName : Microsoft.NET.Native.Runtime.1.4_8wekyb3d8bbwe
PublisherId       : 8wekyb3d8bbwe
IsResourcePackage : False
IsBundle          : False
IsDevelopmentMode : False
NonRemovable      : False
IsPartiallyStaged : False
SignatureKind     : Store
Status            : Ok

$package_dependencies = $packages.Dependencies
$package_rule = New-CIPolicyRule -Package $packages[0] #repeat for all desired packages in the array
$package_rule += New-CIPolicyRule -Package $package_dependencies[0] # repeat for all dependencies in the array
$package_rule

Name           : Microsoft.NET.Native.Runtime.1.4_8wekyb3d8bbwe FileRule
Id             : ID_ALLOW_A_1
TypeId         : Allow
Root           :
FileVersionRef :
AppIDRef       :
Wellknown      : False
Ekus           :
Exceptions     :
FileAttributes :
FileException  : False
UserMode       : True
attributes     : {[AppIDs, ], [MinimumFileVersion, 0.0.0.0], [PackageFamilyName,
                 Microsoft.NET.Native.Runtime.1.4_8wekyb3d8bbwe], [PackageVersion, 1.4.24201.0]}

Name           : Microsoft.NET.Native.Framework.2.2_8wekyb3d8bbwe FileRule
Id             : ID_ALLOW_A_2
TypeId         : Allow
Root           :
FileVersionRef :
AppIDRef       :
Wellknown      : False
Ekus           :
Exceptions     :
FileAttributes :
FileException  : False
UserMode       : True
attributes     : {[AppIDs, ], [MinimumFileVersion, 0.0.0.0], [PackageFamilyName,
                 Microsoft.NET.Native.Framework.2.2_8wekyb3d8bbwe], [PackageVersion, 2.2.29512.0]}
```

这组命令会查找名称与指定值匹配的打包应用程序，并为该应用程序及其依赖项生成一条允许访问（或使用）的规则。


## 参数

### -AllowFileNameFallbacks
表示那些没有 `OriginalFileName` 的文件将按以下顺序进行处理：

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

### -AppID
Specifies an app.
This cmdlet creates per-app rules which control whether specific plug-ins, add-ins, and modules can run from specific apps.

For more information, see [Use a Windows Defender Application Control policy to control specific plug-ins, add-ins, and modules](/windows/security/threat-protection/windows-defender-application-control/use-windows-defender-application-control-policy-to-control-specific-plug-ins-add-ins-and-modules).

```yaml
Type: String
Parameter Sets: DriverFilePath
Aliases:

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

### -DriverFilePath
Specifies the path of a driver on which this cmdlet bases a rule.

```yaml
Type: String[]
Parameter Sets: DriverFilePath
Aliases:

Required: True
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
Parameter Sets: DriverFileList
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
The acceptable values for this parameter are the same as for the **Level** parameter.
If you specify multiple fallback levels, this cmdlet tries them in order.

```yaml
Type: RuleLevel[]
Parameter Sets: (All)
Aliases:
Accepted values: None, Hash, FileName, FilePath, SignedVersion, PFN, Publisher, FilePublisher, LeafCertificate, PcaCertificate, RootCertificate, WHQL, WHQLPublisher, WHQLFilePublisher

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FilePathRule
Specifies the path of a folder for generating a rule with level set to FilePath. Refer to [Filepath Rules Info](/windows/security/threat-protection/windows-defender-application-control/select-types-of-rules-to-create#more-information-about-filepath-rules) for acceptable wildcard values and usage.
This cmdlet will not check whether the filepath string is a valid filepath.

```yaml
Type: String
Parameter Sets: ManualFilePath
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True
Accept wildcard characters: True
```

### -Level
Specifies the primary level of detail for generated rules. Refer to [WDAC File Rule Levels](/windows/security/threat-protection/windows-defender-application-control/select-types-of-rules-to-create#windows-defender-application-control-file-rule-levels) for acceptable parameter values and descriptions.

```yaml
Type: RuleLevel
Parameter Sets: DriverFileList, DriverFilePath
Aliases: l
Accepted values: None, Hash, FileName, FilePath, SignedVersion, PFN, Publisher, FilePublisher, LeafCertificate, PcaCertificate, RootCertificate, WHQL, WHQLPublisher, WHQLFilePublisher

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Package
Specifies the packaged app (MSIX/Appx) to base the rule.

```yaml
Type: AppxPackage
Parameter Sets: PackageFamilyName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ScriptFileNames

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
Specifies the attribute of the file off which to base a file name rule. The -Level must be set to FileName for this option.
Refer to [File Name Rules Info](/windows/security/threat-protection/windows-defender-application-control/select-types-of-rules-to-create#windows-defender-application-control-filename-rules) for a description of the acceptable values.

```yaml
Type: FileNameLevel
Parameter Sets: (All)
Aliases:
Accepted values: None, OriginalFileName, InternalName, FileDescription, ProductName, PackageFamilyName

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

### 规则
这个cmdlet会返回它创建的规则。

## 备注

## 相关链接

[Get-SystemDriver](./Get-SystemDriver.md)
