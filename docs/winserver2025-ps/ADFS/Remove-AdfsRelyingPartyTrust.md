---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfsrelyingpartytrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsRelyingPartyTrust
---

# 移除依赖 AdFS 的主体信任（Remove-AdfsRelyingPartyTrust）

## 摘要
从联邦服务中移除一个依赖方信任（relying party trust）。

## 语法

### 标识符
```
Remove-AdfsRelyingPartyTrust -TargetIdentifier <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 标识符Object
```
Remove-AdfsRelyingPartyTrust -TargetRelyingParty <RelyingPartyTrust> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 标识符Name
```
Remove-AdfsRelyingPartyTrust -TargetName <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Remove-AdfsRelyingPartyTrust** cmdlet 用于从联合服务（Federation Service）中删除依赖方信任关系（relying party trust）。

## 示例

### 示例 1：移除依赖方信任（Removing a Relying Party Trust）
```
PS C:\> Remove-AdfsRelyingPartyTrust -TargetName "FabrikamApp"
```

该命令删除了名为“FabrikamApp”的依赖方信任关系。

## 参数

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -TargetIdentifier
指定要删除的依赖方信任（relying party trust）的标识符。

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
指定要删除的依赖方信任（relying party trust）的名称。

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

### -TargetRelyingParty
用于指定一个 **RelyingPartyTrust** 对象。该 cmdlet 会删除您指定的依赖方信任关系。若要获取一个 **RelyingPartyTrust** 对象，可以使用 **Get-AdfsRelyingPartyTrust** cmdlet。

```yaml
Type: RelyingPartyTrust
Parameter Sets: IdentifierObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前会提示您确认是否要继续执行。

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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

字符串对象通过*TargetIdentifier*和*TargetName*参数被接收。

### Microsoft IdentityServer.PowerShell.Resources.RelyingPartyTrust

`RelyingPartyTrust` 对象是通过 `TargetRelyingParty` 参数接收到的。

## 输出

### Microsoft IdentityServer.PowerShell.Resources.RelyingPartyTrust

当指定*PassThru*参数时，会返回被移除的RelyingPartyTrust对象。默认情况下，此cmdlet不会生成任何输出。

## 备注
* A relying party in Active Directory Federation Services (AD FS) is an organization in which Web servers that host one or more Web-based applications reside. Tokens and Information Cards that originate from a claims provider can be presented and ultimately consumed by the Web-based resources that are located in the relying party organization. When AD FS is configured in the role of the relying party, it acts as a partner that trusts a claims provider to authenticate users. Therefore, the relying party consumes the claims that are packaged in security tokens that come from users in the claims provider. In other words, a relying party is the organization whose Web servers are protected by the resource-side federation server. The federation server in the relying party uses the security tokens that the claims provider produces to issue tokens to the Web servers that are located in the relying party.

## 相关链接

[Add-AdfsRelyingPartyTrust](./Add-AdfsRelyingPartyTrust.md)

[禁用 AdfsRelyingPartyTrust](./ Disable-AdfsRelyingPartyTrust.md)

[Enable-AdfsRelyingPartyTrust](./Enable-AdfsRelyingPartyTrust.md)

[Get-AdfsRelyingPartyTrust](./Get-AdfsRelyingPartyTrust.md)

[Set-AdfsRelyingPartyTrust](./Set-AdfsRelyingPartyTrust.md)

[更新：AdfsRelyingPartyTrust](./Update-AdfsRelyingPartyTrust.md)

