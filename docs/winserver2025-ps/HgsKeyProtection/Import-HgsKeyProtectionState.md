---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.KpsServer.Administration.dll-Help.xml
Module Name: HgsKeyProtection
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgskeyprotection/import-hgskeyprotectionstate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-HgsKeyProtectionState
---

# 导入 HGS 密钥保护状态相关的数据

## 摘要
导入之前导出的密钥保护服务（Key Protection Service）配置文件和证书。

## 语法

### 文件
```
Import-HgsKeyProtectionState -Password <SecureString> [-Force] [-IgnoreImportFailures] [[-Path] <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### XML
```
Import-HgsKeyProtectionState -Password <SecureString> [-Force] [-IgnoreImportFailures] [[-Xml] <XmlDocument>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Import-HgsKeyProtectionState` cmdlet 用于从由 `path` 参数引用的文件中导入之前导出的 Key Protection Service 配置信息。如果未提供 `path` 参数，则可以通过将配置状态作为 `XmlDocument` 对象传递给 `Xml` 参数来导入该配置。如果配置中包含以 PFX 格式添加到服务中的证书（这些证书包含私钥），那么 cmdlet 也会导入这些证书；同样地，如果配置中包含之前以 PFX 格式添加到 Key Protection Service 中的证书，则必须提供的密码要与导出配置时使用的密码相匹配。

## 示例

### 示例 1：从文件中导入密钥保护服务的状态
```
PS C:\> Import-HgsKeyProtectionState -Path "C:\example\kps.config" -Password $Password
```

此命令将配置状态从路径参数所引用的文件导入到密钥保护服务中。如果该文件包含证书的私钥，则必须通过 `$Password` 变量引用一个安全的字符串来提供密码。

### 示例 2：从 XML 文档中导入密钥保护服务的状态信息
```
PS C:\> Import-HgsKeyProtectionState -Xml $XmlDoc -Password $Password
```

此命令从由XML参数引用的XML文档中导入配置状态到密钥保护服务（Key Protection Service）。如果该文件包含证书的私钥，则必须使用$Password变量所引用的安全字符串来提供密码。

## 参数

### -Force
强制命令运行，而无需请求用户确认。

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

### -IgnoreImportFailures
表示此 cmdlet 会忽略导入失败的情况。

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

### -Password
```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
```yaml
Type: String
Parameter Sets: File
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Xml
```yaml
Type: XmlDocument
Parameter Sets: XML
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONPARAMETERS（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### 无
您不能将输入内容通过管道（pipe）传递给此cmdlet。

## 输出

### 无
这个cmdlet不会生成任何输出。

## 备注

## 相关链接

[Export-HgsKeyProtectionState](./Export-HgsKeyProtectionState.md)

