---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ConfigCI.Commands.dll-Help.xml
Module Name: ConfigCI
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/configci/merge-cipolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Merge-CIPolicy
---

# 合并CIP政策

## 摘要
将这些规则合并到多个代码完整性策略文件中。

## 语法

```
Merge-CIPolicy [-OutputFilePath] <String> [-PolicyPaths] <String[]> [-Rules <Rule[]>] [-AppIdTaggingPolicy]
 [<CommonParameters>]
```

## 描述
`Merge-CIPolicy` cmdlet 将多个代码完整性（Code Integrity）策略文件中的规则合并成一个统一的 `.xml` 政策文件。你可以指定要添加到合并后的列表中的规则，但该 cmdlet 会自动删除重复的规则。此外，它还会在规则的 ID 后添加一个数字，以确保每个规则的 ID 都是唯一的。

## 示例

#### 示例 1：合并策略
```
PS C:\> Merge-CIPolicy -PolicyPaths '.\Policy.xml','.\Policy02.xml' -OutputFilePath '.\MergedPolicy.xml'

Name           : MSIT Test CodeSign CA 3
Id             : ID_SIGNER_S_17_0
TypeId         : Allow
Root           : FA6B9A2230CE08BCA81D096B28CF495672401D3A43A0D285CF352464A6C9C7FD
FileVersionRef :
Wellknown      : False
Ekus           :
Exceptions     :
FileAttributes :
FileException  : False
UserMode       : False

Name           : VeriSign Class 3 Code Signing 2010 CA
Id             : ID_SIGNER_S_1D_0
TypeId         : Allow
Root           : 4843A82ED3B1F2BFBEE9671960E1940C942F688D
FileVersionRef :
Wellknown      : False
Ekus           :
Exceptions     :
FileAttributes :
FileException  : False
UserMode       : False

Name           : Microsoft Windows Third Party Component CA 2012
Id             : ID_SIGNER_S_1E_0
TypeId         : Allow
Root           : CEC1AFD0E310C55C1DCC601AB8E172917706AA32FB5EAF826813547FDF02DD46
FileVersionRef :
Wellknown      : False
Ekus           :
Exceptions     :
FileAttributes :
FileException  : False
UserMode       : False

Name           : \\?\E:\cmdlets\temp\Microsoft.ConfigCI.Commands.dll Hash Sha1
Id             : ID_ALLOW_A_49_1
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

这个命令将两个.xml文件中定义的策略合并到第三个文件MergedPolicy.xml中。该cmdlet会在第一个策略中的规则ID后加上“_0”（例如：ID_SIGNER_S_17_0），在第二个策略中的规则ID后加上“_1”（例如：ID_ALLOW_A_49_1）。命令会自动去除重复的规则。在这个示例中，我们仅展示前几条规则。

## 参数

### -AppIdTaggingPolicy
此参数保留以供将来使用。

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

### -OutputFilePath
指定合并后的.xml策略文件的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases: o

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PolicyPaths
指定一个包含 `.xml` 政策文件的路径数组，该 cmdlet 会将这些文件合并在一起。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: p

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Rules
指定一个由 **Rule** 对象组成的数组，该数组将被此 cmdlet 添加到合并后的策略中。要获取一个规则对象，请使用 **Get-CIPolicy** 或 **New-CIPolicyRule** cmdlet。

```yaml
Type: Rule[]
Parameter Sets: (All)
Aliases: r

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 规则
此cmdlet会返回它所创建的政策中的规则。

## 备注

## 相关链接

[Get-CIPolicy](./Get-CIPolicy.md)

[New-CIPolicy](./New-CIPolicy.md)

