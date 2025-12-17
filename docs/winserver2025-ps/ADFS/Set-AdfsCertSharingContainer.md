---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfscertsharingcontainer?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsCertSharingContainer
---

# 设置 AdfsCertSharingContainer

## 摘要
设置用于在联邦服务器群中共享托管证书的账户。

## 语法

```
Set-AdfsCertSharingContainer -ServiceAccount <String> [-Credential <PSCredential>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-AdfsCertSharingContainer` cmdlet 用于设置用于共享 Active Directory Federation Services (AD FS) 2.0 生成和管理的证书的私钥的服务账户。

## 示例

## 参数

### -Credential
用于指定一个凭据对象。要获取一个 **PSCredential** 对象，请使用 **Get-Credential** cmdlet。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ServiceAccount
指定用于共享私钥的服务账户。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注
* Active Directory Federation Services (AD FS) 2.0 does not share the private keys of administrator-specified certificates in a federation server farm, such as certificates that a certification authority (CA) issues.

## 相关链接

