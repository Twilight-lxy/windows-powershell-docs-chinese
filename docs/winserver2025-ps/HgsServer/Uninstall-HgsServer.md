---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: HgsServer-help.xml
Module Name: HgsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsserver/uninstall-hgsserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Uninstall-HgsServer
---

# 卸载 HgsServer

## 摘要
从Host Guardian服务中以及该域名中删除一个本地节点。

## 语法

```
Uninstall-HgsServer [-LocalAdministratorPassword] <SecureString> [-HgsDomainCredential <PSCredential>] [-Force]
 [-Restart] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Uninstall-HgsServer` cmdlet 用于从 Host Guardian Service (HGS) 中删除本地节点。

此 cmdlet 会进行以下配置更改，以便从额外的 HGS 节点中删除 HGS 配置：

- Unregisters the Attestation Service web application with the IIS service.
- Unregisters the Key Protection Service web application with the IIS service.
- Disables Just Enough Administration on the local node.
- Removes the local node from the existing failover cluster.
- Removes the local node from being a domain controller.

This cmdlet makes the following configuration changes in order to remove the HGS configuration from the last HGS node:

- Unregisters the Attestation Service web application with the IIS service.
- Unregisters the Key Protection Service web application with the IIS service.
- Removes the distributed network name (DNN) resource corresponding to the HGS name.
- Disables Just Enough Administration on the local node.
- Destroys the cluster on the local node.
- Removes the local node from being a domain controller and removes the HGS domain.

有关该场景术语的更多信息，请参阅[安全与保障](https://go.microsoft.com/fwlink/?LinkId=699209)。

## 示例

### 示例 1：从 HGS 中删除该节点
```
PS C:\> $Cred = Get-Credential
PS C:\> Uninstall-HgsServer -HgsDomainCredential $cred -LocalAdministratorPassword $secureString
```

这个示例用于从现有的HGS（High Availability Storage）设置中删除某个节点。如果第二个命令删除了最后一个节点，那么整个集群也会被销毁。

## 参数

### -Force
强制命令运行，而不会询问用户的确认。

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

### -HgsDomainCredential
指定用于主HGS服务器的Active Directory域管理员凭据。

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

### -LocalAdministratorPassword
当计算机不再作为域控制器时，用于指定本地管理员账户的密码。

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Restart
表示在执行此命令后，系统会自动重新启动。

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

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

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
展示了如果该cmdlet被运行会发生什么情况。但实际上这个cmdlet并没有被运行。

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

## 输出

## 备注

## 相关链接

[HGS 服务器 cmdlet](./hgsserver.md)

