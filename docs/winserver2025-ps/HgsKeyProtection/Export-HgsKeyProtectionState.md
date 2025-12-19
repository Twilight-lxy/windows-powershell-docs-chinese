---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.KpsServer.Administration.dll-Help.xml
Module Name: HgsKeyProtection
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgskeyprotection/export-hgskeyprotectionstate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-HgsKeyProtectionState
---

# Export-HgsKeyProtectionState

## 摘要
导出密钥保护服务（Key Protection Service）的配置信息和证书。

## 语法

```
Export-HgsKeyProtectionState [-Path <String>] -Password <SecureString> [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Export-HgsKeyProtectionState` cmdlet 将 Key Protection Service 的配置信息导出到由路径参数指定的文件中。如果未提供路径参数，该 cmdlet 会以 XML 格式输出配置状态。如果配置中包含通过 pfx 格式添加到服务中的证书（这些证书包含了私钥），那么导出的配置文件中也會包含这些私钥。`Password` 参数用于保护配置文件中的私钥；如果配置中包含存储在硬件安全模块 (HSM) 中的带有私钥的证书，那么配置文件中仅会包含相应的公钥。

## 示例

### 示例 1：将密钥保护服务的状态导出到文件中
```
PS C:\> Export-HgsKeyProtectionState -Path "C:\example\kps.config" -Password $Password
```

此命令用于导出密钥保护服务（Key Protection Service）的配置状态。所有以.pfx格式添加的证书都会被包含在输出结果中，该输出结果会被写入由路径参数指定的文件中。私钥会使用 `$Password` 安全字符串中指定的密码进行加密保护。

### 示例 2：将 Key Protection Service 的状态导出为 XML 文件
```
PS C:\> Export-HgsKeyProtectionState  -Password $Password
```

此命令会将密钥保护服务（Key Protection Service）的配置状态导出为可供存储在变量中的输出文件。所有以 PFX 格式添加的证书都会包含在该输出文件中。私钥会使用 `$Password` 安全字符串中指定的密码进行加密保护。

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

### -Password
指定用于保护导出配置中包含的私钥的密码。

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
指定用于写入配置状态的文件的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无
您不能将输入数据通过管道传递给这个cmdlet。

## 输出

### 无
如果未指定 `Path` 参数，此 cmdlet 会输出一个 `XmlDocument`，其中包含密钥保护服务（Key Protection Service）的状态信息。

## 备注

## 相关链接

[Import-HgsKeyProtectionState](./Import-HgsKeyProtectionState.md)

