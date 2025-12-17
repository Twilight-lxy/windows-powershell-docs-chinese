---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Deployment.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/test-adfsfarmbehaviorlevelraise?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-AdfsFarmBehaviorLevelRaise
---

# 测试 AdfsFarm 行为级别提升（Test-AdfsFarmBehaviorLevelRaise）

## 摘要
测试你是否能够提升农场的行为水平（即农场内动物或植物的行为表现）。

## 语法

### AdfsUpgradeServiceAccount（默认值）
```
Test-AdfsFarmBehaviorLevelRaise [-Member <String[]>] [-Credential <PSCredential>]
 [-ServiceAccountCredential <PSCredential>] [-Force] [<CommonParameters>]
```

### AdfsUpgradeGmsaAccount
```
Test-AdfsFarmBehaviorLevelRaise [-Member <String[]>] [-Credential <PSCredential>]
 [-GroupServiceAccountIdentifier <String>] [-Force] [<CommonParameters>]
```

## 描述
`Test-AdfsFarmBehaviorLevelRaise` cmdlet 用于测试 `Invoke-AdfsFarmBehaviorLevelRaise` cmdlet 是否能够提升 Active Directory Federation Services (AD FS) 农场的行为级别，从而启用 Windows 操作系统后续版本中提供的新功能。

要测试使用 SQL Server 作为策略数据库的农场的“行为级别”（即农场的安全或管理设置），请指定 *Credential* 参数。

## 示例

#### 示例 1：测试提升农场行为等级的功能
```
PS C:\> Test-AdfsFarmBehaviorLevelRaise
```

这个命令用于测试你是否能够提升农场行为等级（farm behavior level）。

## 参数

### -Credential
用于指定在将 SQL Server 作为策略数据库的 AD FS 农场中运行此 cmdlet 所需的凭据。提供的凭据必须是每台 AD FS 服务器上的管理员权限。要获取一个 **PSCredential** 对象，请使用 **Get-Credential** cmdlet。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Invoke-AdfsFarmBehaviorLevelRaise](./Invoke-AdfsFarmBehaviorLevelRaise.md)

[Restore-AdfsFarmBehaviorLevel](./Restore-AdfsFarmBehaviorLevel.md)

[Test-AdfsFarmBehaviorLevelRestore](./Test-AdfsFarmBehaviorLevelRestore.md)

