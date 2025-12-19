---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/export-iscsitargetserverconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-IscsiTargetServerConfiguration
---

# 导出 iScsiTargetServer 配置信息

## 摘要
导出iSCSI目标服务器配置信息。

## 语法

```
Export-IscsiTargetServerConfiguration [-Filename] <String> [[-ComputerName] <String>] [[-Credential] <String>]
 [-Force] [<CommonParameters>]
```

## 描述
`Export-IscsiTargetServerConfiguration` cmdlet 用于导出 Microsoft iSCSI 目标服务器的配置信息。您可以使用此 cmdlet 来备份 iSCSI 目标服务器的配置，或者创建一个文件以便后续通过 `Import-IscsiTargetServerConfiguration` cmdlet 进行导入。

配置信息包括以下内容：

- If the cmdlet exports the configuration from a clustered iSCSI Target Server instance, the resource group name.
- For an import of the configuration into an iSCSI Target Server clustered instance, the name of the resource group into which to import the configuration.
This resource group name is the same as the iSCSI virtual disk attribute named **MigrationResourceGroup**.
- The following attributes for each iSCSI target that iSCSI Target Server hosts: **Enabled** (target state), **HostName**, **TargetIQN**, **Description**, **ResourceGroup**, **MigrationResourceGroup**, **EnforceIdleTimeoutDetection**, **FirstBurstLength**, **MaxBurstLength**, **MaxRecvDataSegmentLength**, **NumRecvBuffers**, **EnableCHAP**, **CHAPUserName**, **EnableReverseCHAP**, **ReverseCHAPUserName**, **InitiatorIDs**, and **LunMappings**.
- The following attributes for each iSCSI virtual disk that iSCSI Target Server recognizes: **DiskId**, **Type**, **Enabled**, **DevicePath**, **ParentPath**, **Description**, **SnapshotStorageSize**, **MigrationDevicePath**, **MigrationParentPath**, and **MigrationResourceGroup**.

`MigrationParentPath` 和 `ParentPath` 的值始终为 `null`。

此 cmdlet 不会导出挑战握手认证协议（CHAP）的密钥、逻辑单元（LU）的快照信息，以及诸如当前会话信息之类的临时状态信息。

## 示例

### 示例 1：导出独立服务器的配置信息
```
PS C:\> Export-IscsiTargetServerConfiguration -Filename "D:\Server07Config.xml" -ComputerName "StandAloneIscsiServer07.Contoso.com" "
```

该命令将独立运行的iSCSI目标服务器的配置信息导出到指定的文件中。

### 示例 2：导出集群服务器的配置信息
```
PS C:\> Export-IscsiTargetServerConfiguration -Filename "D:\Server07Config.xml" -ComputerName "ClusteredIscsiInstance07.Contoso.com" -Force
```

此命令会将集群化iSCSI目标服务器的配置信息导出到指定的文件中。该命令使用了“Force”参数，因此会直接覆盖现有文件，而不会先提示用户确认。

### 示例 3：导出指定节点中所有集群服务器的配置信息
```
PS C:\> Export-IscsiTargetServerConfiguration -Filename "D:\Node22config.xml" -ComputerName "Node22-iSCSIServer.Contoso.com"
```

该命令将所有托管在指定集群节点上的集群化iSCSI目标服务器实例的配置信息导出到一个指定的文件中。

## 参数

### -ComputerName
如果此 cmdlet 在远程计算机上运行，则会指定远程计算机的名称或 IP 地址。

如果此cmdlet在集群配置上运行，则指定集群资源组的网络名称或集群节点的名称。

该cmdlet会导出在您指定的计算机或集群上运行的iSCSI目标服务器实例的配置信息。如果您没有为该参数指定值，cmdlet将使用本地计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定在连接到远程计算机时所需的凭据信息。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Filename
指定一个文件名。该cmdlet会将配置内容导出到您指定的文件中。如果目标文件已经存在，在您确认操作后，cmdlet会覆盖该文件；如果您指定了*Force*参数，则cmdlet会在不进行确认的情况下直接覆盖文件。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
表示该cmdlet会在不进行确认的情况下覆盖现有的导出文件。

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

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Import-IscsiTargetServerConfiguration](./Import-IscsiTargetServerConfiguration.md)

