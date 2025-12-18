---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ConfigCI.Commands.dll-Help.xml
Module Name: ConfigCI
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/configci/get-cipolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-CIPolicy
---

# Get-CIPolicy

## 摘要
获取代码完整性策略中的规则。

## 语法

```
Get-CIPolicy [-FilePath] <String> [<CommonParameters>]
```

## 描述
`Get-CIPolicy` cmdlet 可以返回代码完整性（Code Integrity）策略中的规则。需要指定一个策略对应的 `.xml` 文件。目前，该 cmdlet 不支持公钥加密标准第 7 版（Public-Key Cryptography Standards #7）格式的策略文件（即 `.p7b` 格式的文件）。

## 示例

#### 示例 1：从策略中获取规则
```
PS C:\> Get-CIPolicy -FilePath '.\Policy.xml'
Name           : MSIT Test CodeSign CA 3
Id             : ID_SIGNER_S_17
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
Id             : ID_SIGNER_S_1D
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
Id             : ID_SIGNER_S_1E
TypeId         : Allow
Root           : CEC1AFD0E310C55C1DCC601AB8E172917706AA32FB5EAF826813547FDF02DD46
FileVersionRef :
Wellknown      : False
Ekus           :
Exceptions     :
FileAttributes :
FileException  : False
UserMode       : False
```

这个命令会从Policy.xml文件中返回规则对象。在这个示例中，我们仅展示前几个规则。

## 参数

### -FilePath
指定此cmdlet获取规则的policy.xml文件的路径。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 规则
此cmdlet会从策略中返回规则。

## 备注

## 相关链接

[Merge-CIPolicy](./Merge-CIPolicy.md)

[New-CIPolicy](./New-CIPolicy.md)

