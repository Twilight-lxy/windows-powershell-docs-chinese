---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Deployment.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/test-adfsfarmbehaviorlevelrestore?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-AdfsFarmBehaviorLevelRestore
---

# 测试 AdfsFarmBehaviorLevelRestore 功能

## 摘要
测试是否可以将 Active Directory Federation Services (AD FS) 系统恢复到之前的运行状态。

## 语法

```
Test-AdfsFarmBehaviorLevelRestore [-Member <String[]>] [-Credential <PSCredential>] -FarmBehavior <Int32>
 [-Force] [<CommonParameters>]
```

## 描述
`Test-AdfsFarmBehaviorLevelRestore` cmdlet用于测试`Restore-AdfsFarmBehaviorLevel` cmdlet是否能够将Active Directory Federation Services (AD FS) 架构恢复到之前的行为级别。

## 示例

## 参数

### -Credential
用于指定运行此cmdlet所需的凭据，该cmdlet适用于使用SQL Server作为策略数据库的AD FS（Active Directory Federation Services）集群。提供的凭据必须具有每台AD FS服务器的管理权限。若要获取一个**PSCredential**对象，请使用**Get-Credential** cmdlet。

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

### -FarmBehavior
指定农场的运行行为（或管理策略）。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: True
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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Invoke-AdfsFarmBehaviorLevelRaise](./Invoke-AdfsFarmBehaviorLevelRaise.md)

[Restore-AdfsFarmBehaviorLevel](./Restore-AdfsFarmBehaviorLevel.md)

[Test-AdfsFarmBehaviorLevelRaise](./Test-AdfsFarmBehaviorLevelRaise.md)

