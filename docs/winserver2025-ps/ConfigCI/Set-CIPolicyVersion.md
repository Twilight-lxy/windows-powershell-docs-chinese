---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ConfigCI.Commands.dll-Help.xml
Module Name: ConfigCI
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/configci/set-cipolicyversion?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-CIPolicyVersion
---

# 设置 CIPolicyVersion

## 摘要
更新策略的版本号。

## 语法

```
Set-CIPolicyVersion -FilePath <String> -Version <String> [<CommonParameters>]
```

## 描述
`Set-CIPolicyVersion` cmdlet 用于更新已签名策略的版本号。在更新已签名的策略时，必须用一个新的策略来替换旧策略；新策略必须在 `UpdatePolicySigners` 属性中指定了签名者，并且其版本号必须大于或等于旧策略的版本号。

## 示例

#### 示例 1：更新策略的版本号
```
PS C:\> Set-CIPolicyVersion -FilePath '.\Policy.xml' -Version '11.1.0.2'
PS C:\> Get-Content -Path '.Policy.xml'
<?xml version="1.0" encoding="utf-8"?>
<SiPolicy xmlns="urn:schemas-microsoft-com:sipolicy">
  <VersionEx>11.1.0.2</VersionEx>
  <PolicyTypeID>{A244370E-44C9-4C06-B551-F6016E563076}</PolicyTypeID>
```

第一个命令将 Policy.xml 的版本修改为 11.1.0.2。

第二个命令用于显示该策略的内容。这个示例展示了策略的前几行内容，其中包含了 **VersionEx** 属性。该属性现在的值为 11.1.0.2。

## 参数

### -FilePath
指定该cmdlet要更新的policy.xml文件的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases: f

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Version
指定用于替换当前策略版本的版本字符串。请按照以下格式输入版本号：整数.整数.整数.整数。**New-CIPolicy** 和 **Merge-CIPolicy** 这两个 cmdlet 创建的策略默认版本号为 10.0.0.0。

```yaml
Type: String
Parameter Sets: (All)
Aliases: v

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Merge-CIPolicy](./Merge-CIPolicy.md)

[New-CIPolicy](./New-CIPolicy.md)

