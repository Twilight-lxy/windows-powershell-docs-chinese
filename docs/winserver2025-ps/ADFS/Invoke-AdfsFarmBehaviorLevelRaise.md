---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Deployment.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/invoke-adfsfarmbehaviorlevelraise?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Invoke-AdfsFarmBehaviorLevelRaise
---

# 调用 Invoke-AdfsFarmBehaviorLevelRaise 命令

## 摘要
提升农场的整体管理水平（或运营水平）。

## 语法

### AdfsUpgradeServiceAccount（默认值）
```
Invoke-AdfsFarmBehaviorLevelRaise [-Member <String[]>] [-Credential <PSCredential>]
 [-ServiceAccountCredential <PSCredential>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### AdfsUpgradeGmsaAccount
```
Invoke-AdfsFarmBehaviorLevelRaise [-Member <String[]>] [-Credential <PSCredential>]
 [-GroupServiceAccountIdentifier <String>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Invoke-AdfsFarmBehaviorLevelRaise` cmdlet 用于提升 Active Directory Federation Services (AD FS) 农场的行为级别，从而启用 Windows 操作系统后续版本中提供的新功能。

要提高使用 SQL Server 作为策略数据库的农场的运行水平，请指定 *Credential* 参数。

## 示例

#### 示例 1：提升农场行为等级
```
PS C:\> Invoke-AdfsFarmBehaviorLevelRaise
```

该命令会将农场行为级别从 Windows Server 2012 R2 升级到 Windows Server 2016 的级别。此命令适用于您所在林中可用的最新版本；无需指定具体的级别。

### 示例 2：提升使用 SQL Server 的农场的农场行为等级
```
PS C:\> $Credentials = Get-Credential
PS C:\> Invoke-AdfsFarmBehaviorLevelRaise -Credential $Credentials
```

第一个命令使用 **Get-Credential** cmdlet 来提示用户输入用户名和密码。该命令将凭据存储在 $Credentials 变量中。

第二个命令将农场行为级别从 Windows Server 2012 R2 升级到 Windows Server 2016 水平。该 cmdlet 指定了存储在 `$Credentials` 变量中的必要凭据。

## 参数

### -Credential
用于指定运行此cmdlet所需的凭据信息，该cmdlet适用于使用SQL Server作为策略数据库的AD FS（Active Directory Federation Services）集群。提供的凭据必须具有每台AD FS服务器的管理员权限。若需获取一个**PSCredential**对象，请使用**Get-Credential** cmdlet。

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

### -Force
强制命令运行，而无需询问用户的确认。

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

### -GroupServiceAccountIdentifier
指定一个组托管服务账户（Group Managed Service Account）的ID。

```yaml
Type: String
Parameter Sets: AdfsUpgradeGmsaAccount
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Member
指定一个成员数组。

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

### -ServiceAccountCredential
指定服务账户的凭据信息。

```yaml
Type: PSCredential
Parameter Sets: AdfsUpgradeServiceAccount
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前，会提示您确认是否要继续执行。

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
展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[ Restore-AdfsFarmBehaviorLevel](./Restore-AdfsFarmBehaviorLevel.md)

[Test-AdfsFarmBehaviorLevelRaise](./Test-AdfsFarmBehaviorLevelRaise.md)

[Test-AdfsFarmBehaviorLevelRestore](./Test-AdfsFarmBehaviorLevelRestore.md)

