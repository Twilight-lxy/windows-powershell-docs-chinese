---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/disable-adfsclaimsprovidertrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-AdfsClaimsProviderTrust
---

# 禁用 AdfsClaimsProviderTrust

## 摘要
禁用联邦服务中对某个声明提供者的信任（即不再信任该声明提供者）。

## 语法

### 标识符Object
```
Disable-AdfsClaimsProviderTrust -TargetClaimsProviderTrust <ClaimsProviderTrust> [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### TokenSigningCertificates
```
Disable-AdfsClaimsProviderTrust -TargetCertificate <X509Certificate2> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 标识符
```
Disable-AdfsClaimsProviderTrust -TargetIdentifier <String> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 标识符Name
```
Disable-AdfsClaimsProviderTrust -TargetName <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Disable-AdfsClaimsProviderTrust` cmdlet 用于禁用联邦服务（Federation Service）中的某个声明提供者（claims provider）的信任关系。一旦被禁用，该声明提供者发出的所有令牌都将不会被 AD FS 服务接受。

## 示例

#### 示例 1：禁用某个声明提供者（claims provider）的信任关系
```
PS C:\> Disable-AdfsClaimsProviderTrust -TargetName "Fabrikam claims provider"
```

此命令将名为“Fabrikam claims provider”的声明提供者信任设置为禁用状态。

## 参数

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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

### -TargetCertificate
指定要禁用的声明提供者信任（claims provider trust）所使用的令牌签名证书。

```yaml
Type: X509Certificate2
Parameter Sets: TokenSigningCertificates
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetClaimsProviderTrust
用于指定一个 **ClaimsProviderTrust** 对象。该cmdlet可启用您所指定的声明提供者信任关系。若要获取一个 **ClaimsProviderTrust** 对象，请使用 **Get-AdfsClaimsProviderTrust** cmdlet。

```yaml
Type: ClaimsProviderTrust
Parameter Sets: IdentifierObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetIdentifier
指定要禁用的声明提供者信任（claims provider trust）的标识符。

```yaml
Type: String
Parameter Sets: Identifier
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetName
指定要禁用的声明提供者信任（claims provider trust）的名称。

```yaml
Type: String
Parameter Sets: IdentifierName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.security cryptography.X509Certificates.X509Certificate.X509Certificate2

`X509Certificate2` 对象是通过 `TargetCertificate` 参数接收到的。

### MicrosoftIdentityServer.PowerShellResourcesClaimsProviderTrust

`ClaimsProviderTrust` 对象是通过 `TargetClaimsProviderTrust` 参数接收到的。

### System.String

字符串对象通过 *TargetIdentifier* 和 *TargetName* 参数被接收。

## 输出

### MicrosoftIdentityServer.PowerShellResourcesClaimsProviderTrust

当指定*PassThru*参数时，会返回一个被禁用的ClaimsProviderTrust对象。默认情况下，此cmdlet不会生成任何输出。

## 备注

## 相关链接

[添加 AdfsClaimsProviderTrust](./Add-AdfsClaimsProviderTrust.md)

[Enable-AdfsClaimsProviderTrust](./Enable-AdfsClaimsProviderTrust.md)

[Get-AdfsClaimsProviderTrust](./Get-AdfsClaimsProviderTrust.md)

[Remove-AdfsClaimsProviderTrust](./Remove-AdfsClaimsProviderTrust.md)

[Set-AdfsClaimsProviderTrust](./Set-AdfsClaimsProviderTrust.md)

[更新 AdfsClaimsProviderTrust](./Update-AdfsClaimsProviderTrust.md)

