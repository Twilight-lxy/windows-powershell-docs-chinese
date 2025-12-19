---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/import-iscsitargetserverconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-IscsiTargetServerConfiguration
---

# 导入IscsiTargetServerConfiguration

## 摘要
导入iSCSI目标服务器配置信息。

## 语法

```
Import-IscsiTargetServerConfiguration [-Filename] <String> [[-ComputerName] <String>] [[-Credential] <String>]
 [-Force] [<CommonParameters>]
```

## 描述
`Import-IscsiTargetServerConfiguration` cmdlet 用于导入 Microsoft iSCSI 目标服务器的配置信息。

配置信息包括以下内容：

- If you exported the configuration from a clustered iSCSI Target Server instance, the resource group name.
- If the cmdlet imports the configuration into an iSCSI Target Server clustered instance, the name of the resource group into which to import the configuration.
This resource group name is the same as the iSCSI virtual disk attribute named **MigrationResourceGroup**.
- The following attributes for each iSCSI target that iSCSI Target Server hosts: **Enabled** (target state), **HostName**, **TargetIQN**, **Description**, **ResourceGroup**, **MigrationResourceGroup**, **EnforceIdleTimeoutDetection**, **FirstBurstLength**, **MaxBurstLength**, **MaxRecvDataSegmentLength**, **NumRecvBuffers**, **EnableCHAP**, **CHAPUserName**, **EnableReverseCHAP**, **ReverseCHAPUserName**, **InitiatorIDs**, and **LunMappings**.
- The following attributes for each iSCSI virtual disk that iSCSI Target Server recognizes: **DiskId**, **Type**, **Enabled**, **DevicePath**, **ParentPath**, **Description**, **SnapshotStorageSize**, **MigrationDevicePath**, **MigrationParentPath**, and **MigrationResourceGroup**.

`MigrationParentPath` 和 `ParentPath` 的值始终为 `null`。

在导入配置之前，请执行以下任务：

- Move the files for all the virtual disks that are eligible for migration from the source server to the destination server.
If there are any file path changes, note the source to destination changes.
- In a cluster configuration, ensure that the destination path of the file copy is on a cluster disk and that the cluster disk has been assigned to the desired iSCSI Target Server resource group, which you created on the destination cluster.
Note the resource group that owns the path.
- If the file paths have changed between the source and the destination servers, open the exported configuration .xml file in a text editor, and identify the **MigrationDevicePath** tags to change to reflect the changes.
- In a cluster configuration, if the file path or the resource group name have changed between the source server and the destination server, open the exported configuration xml file in a text editor, and identify the **MigrationResourceGroup** tags to change to reflect the new resource group.

导入配置文件后，请执行以下操作：

- You must manually reconfigure the forward and reverse Challenge Handshake Authentication Protocol (CHAP) secret keys.
- Because importing does not include logical unit (LU) snapshot information, you must take necessary snapshots.
- Manually apply any iSNS settings that are relevant to the new configuration.
- Manually apply any iSCSI target portal settings that are relevant to the new configuration.

## 示例

### 示例 1：将配置导入当前计算机或集群中
```
PS C:\> Import-IscsiTargetServerConfiguration -Filename "D:\ServerConfig78.xml"
```

该命令从指定的文件中导入单个独立iSCSI目标服务器或多个集群化iSCSI目标服务器的配置信息。这些配置会被导入到当前使用的独立计算机或集群节点中。

### 示例 2：将配置导入指定的计算机或集群
```
PS C:\> Import-IscsiTargetServerConfiguration -Filename "D:\ServerConfig78.xml" -ComputerName "TargetServer09.Contoso.com"
```

该命令从指定的文件中导入单个 iSCSI 目标服务器或集群式 iSCSI 目标服务器的配置信息。这些配置信息随后会被导入到指定的远程独立计算机或远程集群节点中。

## 参数

### -ComputerName
如果此 cmdlet 在远程计算机上运行，则会指定该远程计算机的名称或 IP 地址。

指定集群资源组的网络名称，或者如果在此cmdlet运行于集群配置上时，指定集群节点的名称。

该cmdlet会将iSCSI目标服务器的配置导入到您指定的计算机或集群中。如果您未指定此参数，那么cmdlet会将该配置导入到在同一台计算机上运行的iSCSI目标服务器中。

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
指定一个文件名。该cmdlet会从您指定的文件中导入配置信息。

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
表示该cmdlet会删除目标节点上具有相同名称或设备路径的现有**iSCSITarget**或**iSCSIVirtualDisk**，然后导入配置文件中的相应项。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Export-IscsiTargetServerConfiguration](./Export-IscsiTargetServerConfiguration.md)

[Set-IscsiServerTarget](./Set-IscsiServerTarget.md)

